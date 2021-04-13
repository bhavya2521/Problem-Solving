from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    c=n//2 + 1
    s=0
    i=n*k-c
    while(k!=0):
        s+=l[i]
        i=i-c
        k-=1
    print(s)