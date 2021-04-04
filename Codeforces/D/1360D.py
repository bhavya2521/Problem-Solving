import bisect
import math
t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a=[]
    b=[]
    for i in range(1, int(math.sqrt(n) + 1)) : 
        if(n%i==0):
            a.append(i)
            if(b==[]):
                b.append(n//i)
            else:
                b.insert(0,n//i)
    a.extend(b)
    res = (bisect.bisect(a, k))
    print(n//a[res-1])