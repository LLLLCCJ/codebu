x=[1,2,3]
def hanoi(x,i,n):
    print(x[0],'->',x[1])
    print(x[0], '->', x[2])
    print(x[1], '->', x[2])
    if n!=i:
        if i%2!=0:
            print(x[0], '->', x[1])
        else:
            print(x[1], '->', x[0])
    else:
        exit()
    temp=x[2]
    x[2]=x[1]
    x[1]=x[0]
    x[0]=temp
    i+=1
    hanoi(x,i,n)
hanoi(x=[1,2,3],i=1,n=4)
