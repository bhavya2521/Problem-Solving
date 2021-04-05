n=int(input())
l=list(map(int,input().split()))
m=l[:]
l.sort()
k=int(input())
for i in range(n-1):
    l[i+1]+=l[i]
    m[i+1]+=m[i]
m.insert(0,0)
l.insert(0,0)
for _ in range(k):
    t,a,b = map(int,input().split())
    if(t==1):
        print(m[b]-m[a-1])
    else:
        print(l[b]-l[a-1])