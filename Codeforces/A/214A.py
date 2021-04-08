import math
n,m=map(int,input().split())
k=int(max(math.sqrt(n),math.sqrt(m)))
c=0
for i in range(k+1):
    for j in range(k+1):
        if(i*i+j == n and j*j+i==m):
            c+=1
print(c)