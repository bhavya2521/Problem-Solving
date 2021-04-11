t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    
    for i in range(1,1025):
        p=[]
        for j in l:
            p.append(i^j)
        p.sort()
        if(l==p):
            print(i)
            c=-1
            break
        else:
            continue
    if(c==0):
        print(-1)