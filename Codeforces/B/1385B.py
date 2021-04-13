from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    p=[]
    for i in l:
        if(i not in p):
            p.append(i)
    for i in p:
        print(i,end=" ")
    print("")