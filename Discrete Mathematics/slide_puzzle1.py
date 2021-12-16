def check(x):
    
def move(x):
    if x==[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]:
        exit()
    for i in range(len(x)):
        if x[i] == 0:
            for j in range(4):
                # down
                if i>4 and j==0:
                    x[i]=x[i-4]
                    x[i-4]=0
                    print('down')
                    print(x)
                    move(x)
                # up
                if i<12 and j==1:
                    x[i]=x[i+4]
                    x[i+4]=0
                    print('up')
                    print(x)
                    move(x)
                #left
                if i%4==3 and j==2:
                    x[i]=x[i+1]
                    x[i+1]=0
                    print('left')
                    print(x)
                    move(x)
                #right
                if i%4==0 and j==3:
                    x[i]=x[i-1]
                    x[i-1]=0
                    print('right')
                    print(x)
                    move(x)
move(x=[5,1,4,8,9,6,3,11,10,2,15,7,13,14,12,0])
