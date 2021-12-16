def up_down(x):
    ask=int(input())
    if x>ask:
        print('x is larger than ask')
        x=(ask+2097151)//2
        up_down(x)
    elif x<ask:
        print('x is smaller than ask')
        x=(ask+1)//2
        up_down(x)
    else:
        print('correct')
        exit()
up_down(x=100)
