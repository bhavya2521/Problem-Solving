from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    a,b,n=map(int,input().split())
    x=min(a,b)
    y=max(a,b)
    c=0
    while(x<=n and y<=n):
        x+=y
        a=min(x,y)
        b=max(x,y)
        x=a
        y=b
        c+=1
    print(c)