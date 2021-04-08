from sys import*
input= stdin.readline
n=int(input())
l=list(map(int,input().split()))
x=0
for i in l:
   x=x^i
if(x==0):
    print("YES")
else:
    print("NO")