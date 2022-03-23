#0=/ 1=\ 2=' '
def check(x):
    i=len(x)-1
    if x.count(2)>9:
        return False
    #왼쪽
    if i%5!=0 and x[i]+x[i-1]==1:
        return False
    #위쪽
    if i>4 and x[i]+x[i-5]==1:
        return False
    #왼위
    if i>5 and i%5!=0 and x[i]==x[i-6] and x[i]+x[i-6]==2:
        return False
    #오위
    if i>4 and i%5!=4 and x[i]+x[i-4]==0:
        return False
    return True

def generator(x):
    if len(x)==25:
        print(x)
        exit()
    for i in range(3):
        x.append(i)
        if check(x):
            generator(x)
        x.pop()

generator(x=[])
