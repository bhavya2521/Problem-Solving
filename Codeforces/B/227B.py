n=int(input())
l=list(map(int,input().split()))
m=int(input())
q=list(map(int,input().split()))
x=[0]*(n+1)
for i in range(n):
    x[l[i]]=i
a=0
b=0
for i in q:
    a+=x[i]+1
    b+=n-x[i]
print(a,b)