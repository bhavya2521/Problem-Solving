from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.insert(0,0)
    m=0
    for i in range(1,n+1):
        c=0
        j=i
        while(i<=n):
            c+=l[i]
            i+=l[i]
        m=max(c,m)
    print(m)