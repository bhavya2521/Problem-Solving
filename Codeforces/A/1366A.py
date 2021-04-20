from sys import*
input= stdin.readline
n=int(input())
for _ in range(n):
    x,y=map(int,input().split())
    a=max(x,y)
    b=min(x,y)
    if(a>=b*2):
        print(b)
    elif(a==0 or b==0):
        print(0)
    else:
        x=(2*b-a)//3
        if((a-x)<(b-2*x)*2):
            x+=1
        print(b-x)