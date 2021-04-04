n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(k-1):
    if(l[i+1]<l[i]):
        c+=1
print(c*n+l[-1]-1)