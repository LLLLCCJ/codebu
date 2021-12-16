def hanoi(n,to,fro,mid):
    if n==1:
        print(to,"<-",fro)
    else:
        hanoi(n-1,mid,fro,to)
        print(to,"<-",fro)
        hanoi(n-1,to,mid,fro)

hanoi(3,3,1,2)
