from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    s=set(l)
    m=len(s)
    if(m==n):
        print(n//2)
    else:
        d={}
        for i in l:
            d[i]=d.get(i,0)+1
        p=list(d.values())
        p.sort(reverse=True)
        if(len(p)==1):
            a=p[0]//2
        else:
            a=max(p[0]//2,p[1])
        print(a)