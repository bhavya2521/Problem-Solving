from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    h,c,t=map(int,input().split())
    d=h-c
    if(t%d==0):
        print((t//d)*2)
    else:
        a=abs((t-h)//(d-t))
        if((t-h)%(d-t)!=0):
            a+=1
        x=abs((a*d+(h))/(a+1)-t)
        y=abs((a*d-(h))/(a-1)-t)
        
        if(x>y):
            print(2*a-1)
        else:
            print(2*a+1)