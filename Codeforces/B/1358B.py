t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    if(l[0]>=2):
        print(1)
        continue
    for i in range(n-1,-1,-1):
        if(l[i]<=i+1):
            break
    print(i+2)