from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(l[0]==n or l[-1]==1):
        print("NO")
    else:
        print("YES")