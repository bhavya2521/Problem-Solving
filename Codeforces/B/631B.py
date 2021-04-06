from sys import*
input= stdin.readline
n,m,k=map(int,input().split())
l=[]
r=[0]*n
c=[0]*m
rt=[0]*n
ct=[0]*m
for i in range(k):
    z,x,y = map(int,input().split())
    if(z==1):
        r[x-1]=y
        rt[x-1]=i+1
    else:
        c[x-1]=y
        ct[x-1]=i+1
for i in range(n):
    for j in range(m):
        if(r[i]==c[j]):
            print(r[i],end=" ")
        elif(rt[i]>ct[j]):
            print(r[i],end=" ")
        else:
            print(c[j],end=" ")
    print("")