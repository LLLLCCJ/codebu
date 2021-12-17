import itertools as it

def is_solution(perm):
    for i,j in it.combinations(range(len(perm)),2):
        if abs(i-j)==abs(perm[i]-perm[j]):
            return False                    
        return True

for perm in it.permutations(range(4)):
    if is_solution(perm):
        print(perm)

