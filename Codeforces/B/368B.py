from sys import*
input= stdin.readline
n,k=map(int,input().split())
l=list(map(int,input().split()))
p=set()
for i in range(1,n+1):
    p.add(l[-i])
    l[-i]=str(len(p))
for _ in range(k):
    h=int(input())
    print(l[h-1])