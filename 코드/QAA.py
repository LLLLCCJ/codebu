import pandas as pd
import networkx as nx
from random import shuffle, random
from copy import deepcopy
import numpy as np

# 문제 불러오기
def load_file(dir):
    def euc_D(coord1,coord2):
        return ((coord1[0]-coord2[0])**2+(coord1[1]-coord2[1])**2)**(1/2)
    data=pd.read_csv(dir,header=None)
    
    data_list=[]
    
    for i in range(len(data)):
        target=data.iloc[i].item().split(" ")
        for j in range(len(target)):
            target[j]=int(target[j])
    
        data_list.append(target)
    
    G=nx.Graph()
    for i in data_list:
        target_idx=i[0]
        target_coord=(i[1],i[2])
        G.add_node(target_idx,coord=target_coord)
    
    for i in range(len(data_list)-1):
        for j in range(i+1,len(data_list)):
            idx1=data_list[i][0]
            idx2=data_list[j][0]
            coord1=(data_list[i][1],data_list[i][2])
            coord2=(data_list[j][1],data_list[j][2])
            G.add_edge(idx1,idx2,weight=euc_D(coord1,coord2))
        
    return G
# random으로 feasible solution 생성
# depot node 1 생략
def init_sol(G,P):
    length=len(G.nodes)
    S=[i for i in range(2,length+1)]
    shuffle(S)
    # depot 삽입
    S.insert(0,1)
    S.append(1)
    replica=[S for _ in range(P)]

    return S, replica

# KNN 각 노드 별 nearest 20 nodes dictionary
# 중복되는 값에 대해 여러 번 계산이 이루어짐. 
# 2와 가장 가까운 노드가 30, 12, 13 일 때, 12, 13, 30을 계산할 때, 2에 대한 계산이 한 번 더 진행됨.
# 해당 부분 수정 가능. 
def KNN(G,k):
    Nodes=G.nodes()
    KNN_Dict={}
    for i in range(1,len(Nodes)+1):
        target=[]
        target_cost=[]
        for j in range(1,len(Nodes)+1):
            if i==j:
              continue
            target.append(j)
            path=nx.dijkstra_path(G,i,j,'weight')
            cost=nx.path_weight(G,path,'weight')
            target_cost.append(cost)
        
        topk_Nodes=[]

        for _ in range(k):
            idx=target_cost.index(min(target_cost))
            topk_Nodes.append(target[idx])
            target_cost[idx]=9999999999999

        KNN_Dict[i]=topk_Nodes

    return KNN_Dict

# 일반적인 cost function.    
def potential_E(G,S):
    length=len(G.nodes)
    spin_matrix=[[-1 for i in range(length)] for i in range(length)]
    C=0
    for i in range(len(S)-1):

        #path=nx.dijkstra_path(G,S[i],S[i+1],'weight')
        path=(S[i],S[i+1])
        # spin matrix update
        for idx in range(len(path)-1):
            spin_matrix[path[idx]-1][path[idx+1]-1]=1
            spin_matrix[path[idx+1]-1][path[idx]-1]=1
        # cost update
        cost=nx.path_weight(G,path,'weight')

        C+=cost
    return C, spin_matrix

# mutation인 2-opt move 적용
def mutation(G, S, spin_matrix, replica, replica_spin_matrix, S_best_cost, replica_cost, KNN_Dict):
    # Calculate about replica
    for current in range(len(replica)):
        S=replica[current]
        S_cost=99999999999999

        best_cost=S_cost
        S_spin_matrix=deepcopy(replica_spin_matrix[current])
        for i in range(len(S)):
            p=S[i]
            q_list=KNN_Dict[p]
            for q in q_list:
                idx_p=S.index(p)
                idx_q=S.index(q)
                
                if idx_p>idx_q:
                    idx_p,idx_q=idx_q,idx_p
                
                target=S[idx_p+1:idx_q]
                target=target[::-1]

                temp_S=S[:idx_p+1]+target+S[idx_q:]

                temp_S_cost,temp_S_spin_matrix=potential_E(G,temp_S)
                
                if temp_S_cost<best_cost:
                    S=deepcopy(temp_S)
                    best_cost=temp_S_cost
                    S_spin_matrix=deepcopy(temp_S_spin_matrix)
        
        replica[current]=deepcopy(S)
        replica_spin_matrix[current]=deepcopy(S_spin_matrix)
        replica_cost[current]=best_cost

    return S, spin_matrix, replica, replica_spin_matrix, S_best_cost, replica_cost

# tunneling effect term: replica들의 ferromagnetic coupling을 측적하여 계산에 이용함.
# gamma: ferromagnetic coupling schedule
def kinetic_E(gamma,replica_spin_matrix):
    length=len(replica_spin_matrix[0])
    SUM=0
    for i in range(len(replica_spin_matrix)-1):
        for j in range(i+1,len(replica_spin_matrix)):
            for k in range(length):
                for kk in range(length):
                    SUM+=replica_spin_matrix[i][k][kk]*replica_spin_matrix[j][k][kk]
    
    return SUM*gamma

# Total Hamiltonian 계산
def HAM(replica_cost,replica_spin_matrix,P,T,gamma):
    
    pot=sum(replica_cost)/P/T
    kin=0
    length=len(replica_spin_matrix[0])
    for i in range(len(replica_spin_matrix)-1):
        for k in range(length):
            for kk in range(length):
                kin+=replica_spin_matrix[i][k][kk]*replica_spin_matrix[i+1][k][kk]

    kin*=gamma

    Energy=np.exp(kin-pot)

    return Energy


# decay rate is determined with number of MC steps
# alpha=T/MC
def QA(T,Tmin,P,k,alpha,beta,gamma,iter,dir):
    # 문제 load
    G=load_file(dir)
    # 초기해 및 초기 replica 생성
    S, replica=init_sol(G,P)
    S_cost,spin_matrix=potential_E(G,S)
    
    replica_spin_matrix=[]
    replica_cost=[]

    for i in replica:
        temp_cost,temp_spin_matrix=potential_E(G,i)
        replica_spin_matrix.append(temp_spin_matrix)
        replica_cost.append(temp_cost)
    best_cost=min(replica_cost)
    KNN_Dict=KNN(G,k)
    print(S)
    print(S_cost)
    # iteration condition: 감쇠율 alpha는 T/MC로 정해짐.
    
    while iter>0:
        # replica와 current solution에 mutation 적용.
        new, new_spin_matrix, new_replica, new_replica_spin_matrix, new_cost, new_replica_cost = mutation(
                                    G,S,spin_matrix,replica,replica_spin_matrix,S_cost,replica_cost,KNN_Dict
                                    )

        # Energy 계산 cost:P_Energy
        Energy=HAM(replica_cost,replica_spin_matrix,P,T,gamma)
        # Metropolis condition 확인.
        rand=random()
        
        minimum=min(new_replica_cost)
        if minimum<best_cost:
            S, spin_matrix, S_cost = new, new_spin_matrix, new_cost
            replica, replica_spin_matrix, replica_cost=new_replica, new_replica_spin_matrix, new_replica_cost
        else:
            if Energy>rand:
                S, spin_matrix, S_cost = new, new_spin_matrix, new_cost
                replica, replica_spin_matrix, replica_cost=new_replica, new_replica_spin_matrix, new_replica_cost
        # T는 고정
        # T*=alpha
        gamma*=beta
        iter-=1
    

    idx=replica_cost.index(min(replica_cost))
    return replica[idx], replica_cost[idx]

alpha=30
gamma=300
P=30
T=10/3
k=20
MC= 100
iter=100
Tmin=100
beta=10
dir="./pr107.txt"

print(QA(T,Tmin,P,k,alpha,beta,gamma,iter,dir))