t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    m=999
    l.sort()
    for i in range(n-1):
        if(l[i+1]-l[i]<m):
            m=l[i+1]-l[i]
    print(m)