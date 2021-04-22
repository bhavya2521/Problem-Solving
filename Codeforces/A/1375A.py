from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    for i in range(n):
        l[i]=abs(l[i])
    for i in range(n):
        if(i%2==0):
            print(l[i],end=" ")
        else:
            print(-l[i],end=" ")
    print("")