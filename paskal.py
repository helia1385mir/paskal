n=int(input())
kha=[[None for i in range(n)]for j in range(n)]#57
# print(kha)

for i in range(n):
    kha[i][0]=1

for i in range(n) :
    kha[i][i]=1

for i in range(2,n):
    for j in range(1,i):
        kha[i][j]=kha[i-1][j]+kha[i-1][j-1]

for i in range(n):
    for j in range(i+1) :
        print(kha[i][j],end=' ')
    print()