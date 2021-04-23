from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    s=set(l)
    n=len(s)
    if(n==3):
        print("NO")
    elif(n==1):
        print("YES")
        print(l[0],l[0],l[0])
    else:
        if(l.count(max(l))!=2):
            print("NO")
        else:
            print("YES")
            print(max(l),min(l),1)