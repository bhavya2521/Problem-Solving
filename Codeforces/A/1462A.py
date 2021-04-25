from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a,b=0,n-1
    while(a<=b):
        if(a==b):
            print(l[a],end=" ")
        else:
            print(l[a],l[b],end=" ")
        a+=1
        b-=1
    print("")