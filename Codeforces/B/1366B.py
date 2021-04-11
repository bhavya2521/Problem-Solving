from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,x,m = map(int,input().split())
    c=0
    d=0
    for _ in range(m):
        a,b=map(int,input().split())
        if(c==0):
            if(a<=x<=b):
                c=a
                d=b
        else:
            if(a<=c<=b or a<=d<=b):
                c=min(a,c)
                d=max(b,d)
    if(c==0):
        print(1)
    else:
        print(d-c+1)