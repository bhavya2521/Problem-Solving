from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    l.insert(0,0)
    for i in range(1,n+1):
        if(i!=l[i] and i-1==l[i-1]):
            c+=1
    if(c==0 or c==1):
        print(c)
    else:
        print(2)