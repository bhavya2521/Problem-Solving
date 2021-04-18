from sys import*
input= stdin.readline
n,m=map(int,input().split())
a=list(map(str,input().split()))
b=list(map(str,input().split()))
t=int(input())
for _ in range(t):
    x=int(input())
    p=(x%n)-1
    q=(x%m)-1
    print(a[p]+b[q])