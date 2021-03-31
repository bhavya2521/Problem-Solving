n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort(reverse=True)
a=0
b=0
t=l[:]
for i in range(n):
    m=max(l)
    l[l.index(m)]-=1
    a+=m
for i in range(n):
    m=min(t)
    t[t.index(m)]-=1
    if(0 in t):
        t.remove(0)
    b+=m
print(a,b)