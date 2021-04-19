t=int(input())
for _ in range(t):
    n=int(input())
    d=2**n
    for i in range(1,(n//2)):
        d+=2**i
    for i in range(n//2,n):
        d-=2**i
    print(d)