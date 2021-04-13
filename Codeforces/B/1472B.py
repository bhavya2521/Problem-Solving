from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    a,b=0,0
    for i in l:
        if(i==1):
            a+=1
        else:
            b+=1
    s=a+2*b
    if(s%2!=0):
        print("NO")
    elif((s//2)%2==0):
        print("YES")
    elif(a>0):
        print("YES")
    else:
        print("NO")