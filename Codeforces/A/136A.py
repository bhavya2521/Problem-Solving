from sys import*
input= stdin.readline
n=int(input())
l=list(map(int,input().split()))
res=[0]*n
for i in range(n):
    res[l[i]-1]=i+1
for i in res:
    print(i,end=" ")