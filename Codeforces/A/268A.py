from sys import*
input= stdin.readline
n=int(input())
a=[]
b=[]
for _ in range(n):
    x,y=map(int,input().split())
    a.append(x)
    b.append(y)
c=0
for i in range(n):
    c+=b[:i].count(a[i])+b[i+1:].count(a[i])
print(c)