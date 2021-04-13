from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m1=min(a)
    m2=min(b)
    c=0
    for i in range(n):
        x=a[i]-m1
        y=b[i]-m2
        c+=max(x,y)
    print(c)