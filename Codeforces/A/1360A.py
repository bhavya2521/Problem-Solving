t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    x = min(a,b)
    y = max(a,b)
    if(x+x >= y):
        print((2*x)**2)
    else:
        print((y)**2)