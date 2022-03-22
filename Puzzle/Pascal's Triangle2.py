C = dict()
for i in range(8):
    C[i, 0] = 1
    C[i, i] = 1
    for j in range(1,i):
        C[i,j]=C[i-1,j-1]+C[i-1,j]
print(C[7,3])
