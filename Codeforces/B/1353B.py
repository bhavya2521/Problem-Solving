t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    if(a[0] >= b[0]):
        print(sum(a))
    else:
        s=0
        c=0
        for i in range(k):
            if(b[i]>a[i]):
                s+=b[i]
            else:
                s+=sum(a[i:])
                c=-1
                break
        if(c==0):
            s+=sum(a[k:])
        
        print(s)