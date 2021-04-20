from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    s=0
    d=[]
    for i in range(n):
        if(l[i]%m!=0):
            c+=1
            d.append(i)
        s+=l[i]
    if(c==0):
        print(-1)
    elif(s%m!=0):
        print(n)
    else:
        left = n-(d[0]+1)
        right = d[-1]
        print(max(left,right))