n,t=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
d=1000
for i in range(t-n+1):
    if(l[i+n-1]-l[i]<d):
        d=l[i+n-1]-l[i]
print(d)