import itertools as it

def five_List(i,res_List):
    for m in range(i):
        res_List.append(5)
    return res_List
def seven_List(i,res_List):
    for m in range(i):
        res_List.append(7)
    return res_List
def generator(x):
    res_List=[]
    for i in range(x//5+1):
        for j in range(x//7+1):
            if x<5*i+7*j:
                break
            if x==5*(i)+7*(j):
                return(seven_List(j,five_List(i,res_List)))
print(generator(x=100))
