import itertools as it
def is_solution(perm):
    for i,j in it.combinations(range(len(perm)),2):
        if abs(i-j)==abs(perm[i]-perm[j]):
            return False
    return True
def list_making(perm,n):
    if len(perm)==n:
        print(perm)
        exit()
    for i in range(n):
        if i not in perm:
            perm.append(i)
            if is_solution(perm):
                list_making(perm,n)
            perm.pop()
list_making(perm=[],n=4)





