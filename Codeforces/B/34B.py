n,m=map(int,input().split())
l=list(map(int,input().split()))
c=0
r=0
l.sort()
for i in l:
    if(c==m or i>=0):
        break
    r+=i
    c+=1
print(-r)