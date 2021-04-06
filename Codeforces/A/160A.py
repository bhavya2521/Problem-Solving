from sys import*
input= stdin.readline
n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
s=sum(l)
x=0
for i in range(n):
    s-=l[i]
    x+=l[i]
    if(x>s):
        print(i+1)
        break