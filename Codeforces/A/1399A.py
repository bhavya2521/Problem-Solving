from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(n==1):
        print("YES")
    else:
        l.sort()
        c=0
        for i in range(n-1):
            if(l[i+1]-l[i]>1):
                c=-1
                break
        if(c==-1):
            print("NO")
        else:
            print("YES")