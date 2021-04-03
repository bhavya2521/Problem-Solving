t=int(input())
for _ in range(t):
    n=int(input())
    if(n==1):
        print(0)
    else:
        n=n//2
        s=n*(n+1)*(2*n+1)//6
        print(8*s)