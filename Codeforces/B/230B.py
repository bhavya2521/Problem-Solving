import math
n=10**6+1
prime = [True for i in range(n)] 
p = 2
while (p * p <= n): 
    if (prime[p] == True): 
        for i in range(p * p, n, p): 
            prime[i] = False
    p += 1
prime[1]=False
n=int(input())
l=list(map(int,input().split()))
for i in l:
    x=int(math.sqrt(i))
    if(x*x == i and prime[x]):
        print("YES")
    else:
        print("NO")