from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    p=list(map(int,input().split()))
    q=list(map(int,input().split()))
    p=set(p)
    q=set(q)
    l=p.intersection(q)
    l=list(l)
    if(l==[]):
        print("NO")
    else:
        print("YES")
        print(1,l[0])