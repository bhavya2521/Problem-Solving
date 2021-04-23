from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    if(2*a<=b):
        print(a,2*a)
    else:
        print(-1,-1)