from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))
    l=[]
    for i in p:
        x=k//i
        if(k%i!=0):
            x+=1
        l.append(x)
    l.sort()
    c=0
    i=0
    left=0
    while(i<n):
        j=i+l[i]-1
        if(j<n and l[j]==l[i]):
            c+=1
            i=j+1
        elif(left>=l[i]-1):
            c+=1
            left-=l[i]-1
            i+=1
        else:
            left+=1
            i+=1
        
    print(c)