from collections import Counter
t=int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    v= list(Counter(l).values())
    p=max(v)
    n=len(set(l))-1
    if(n>=p):
        print(p)
    else:
        print(p-1)