def change(x,chan):
    a,b=chan
    x[a],x[b]=x[b],x[a]

x=['s','t','o','p']
chan=[(0,1),(1,2),(2,3)]

for i in chan:
    change(x,i)
print(x)
