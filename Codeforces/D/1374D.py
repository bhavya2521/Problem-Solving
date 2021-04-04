from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    a={}
    s=0
    for i in l:
        x=i
        if(i%k!=0):
            x=k-(i%k)
            a[x]=a.get(x,0)+1
    for key,value in a.items():
        s=max(s,key+(value-1)*k)
    if(s==0):
        print(0)
    else:
        print(s+1)