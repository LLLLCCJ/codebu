import itertools as it
def app(x,n,k):
    if n == k:
        exit()
    for i in range(n):
        if i==0 or i==n-1:
            x.append(1)
        else:
            z=x[len(x)-n]+x[len(x)+1-n]
            x.append(z)
    n+=1
    if n<=k:
        app(x,n,k)
    return (x)
print(app(x=[1],n=2,k=4))
