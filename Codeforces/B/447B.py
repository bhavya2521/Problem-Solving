from sys import*
input= stdin.readline
s=input()
d=int(input())
l=list(map(int,input().split()))
m=max(l)
n=len(s.strip())
c=0
for i in range(n):
    x=ord(s[i])-97
    c+=l[x]*(i+1)
for i in range(n+1,n+d+1):
    c+=(m*i)
print(c)