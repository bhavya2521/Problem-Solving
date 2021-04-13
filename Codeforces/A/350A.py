n,m=map(int,input().split())
p=list(map(int,input().split()))
f=list(map(int,input().split()))
p.sort()
f.sort()
c=0
for t in range(p[-1],f[0]):
    if(2*p[0]<=t):
        print(t)
        c=-1
        break
if(c==0):
    print(-1)