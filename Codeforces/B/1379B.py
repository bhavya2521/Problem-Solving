from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    l,r,m=map(int,input().split())
    a=max(m//r,1)
    m-=a*r
    print(a,r,r-m)