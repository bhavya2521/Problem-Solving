from sys import*
input= stdin.readline
n,m,d=map(int,input().split())
l=[]
for _ in range(n):
    h=list(map(int,input().split()))
    l.extend(h)
k=l[0]%d
c=0
for i in range(n*m):
    if(l[i]%d!=k):
        print(-1)
        c=-1
        break
if(c==0):
    l.sort()
    median=l[(n*m-1)//2]
    for i in l:
        c+=abs(i-median)//d
    print(c)