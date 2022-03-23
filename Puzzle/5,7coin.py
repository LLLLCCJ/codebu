# making 46 with 5-coin and 7-coin
def check(x,L):
    for i in range(x//5+1):
        for j in range(x//7+1):
            if x==5*i+7*j:
                List_maker(L,i,j)
def List_maker(L,i,j):
    for m in range(i):
        L.append(5)
    for n in range(j):
        L.append(7)
    L.sort()
    print(L)

check(46,L=[])
