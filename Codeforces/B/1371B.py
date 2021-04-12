from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,r=map(int,input().split())
    c=min(n,r)
    if(c==n):
        c-=1
        print((c*(c+1)//2)+1)
    else:
         print(c*(c+1)//2)