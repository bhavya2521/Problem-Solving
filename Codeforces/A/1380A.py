from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for i in range(1,n-1):
        if(l[i]>l[i+1] and l[i]>l[i-1]):
            c=-1
            print("YES")
            print(i,i+1,i+2)
            break
    if(c==0):
        print("NO")