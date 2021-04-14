n,k = map(int,input().split())
l=list(map(int,input().split()))
d=0
r=n-1
m=0
for i in range(n):
    d=l[i]//k
    if(l[i]%k!=0):
        d+=1
    if(d>=m):
        r=i
        m=d
print(r+1)