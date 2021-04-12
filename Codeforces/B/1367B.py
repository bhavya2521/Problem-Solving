t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    e=[]
    o=[]
    for i in range(n):
        if(i%2!=l[i]%2):
            if(l[i]%2==0):
                e.append(i)
            else:
                o.append(i)
    even=len(e)
    odd=len(o)
    if(even==odd):
        print(even)
    else:
        print(-1)