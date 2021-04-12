from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    x=0
    l=[]
    for _ in range(n):
        h=list(map(int,input().split()))
        l.append(h)
    a=[]
    for i in range(m):
        if(i==0):
            a.append(2)
        elif(i==m-1):
            a.append(2)
        else:
            a.append(3)
    b=[]
    for i in range(m):
        if(i==0):
            b.append(3)
        elif(i==m-1):
            b.append(3)
        else:
            b.append(4)
    d=0
    for i in range(n):
        for j in range(m):
            if(i==0 or i==n-1):
                if(l[i][j]>a[j]):
                    d=-1
                    break
            else:
                if(l[i][j]>b[j]):
                    d=-1
                    break
        if(d==-1):
            break
    if(d==-1):
        print("NO")
    else:
        print("YES")
        for i in range(n):
            if(i==0 or i==n-1):
                for p in a:
                    print(p,end=" ")
            else:
                for p in b:
                    print(p,end=" ")
            print("")