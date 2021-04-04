n,k=map(int,input().split())
l=list(map(int,input().split()))
c=1
s=sum(l[:k])
j=0
r=100*k
for i in range(k,n):
    s+=l[i]-l[j]
    j+=1
    if(s<r):
        r=s
        c=j+1
    
print(c)