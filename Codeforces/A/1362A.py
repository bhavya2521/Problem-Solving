n=int(input())
def cal(d):
    r=0
    while(d%8==0):
        r+=1
        d=d//8
    while(d%4==0):
        r+=1
        d=d//4
    while(d%2==0):
        r+=1
        d=d//2
    return(r)
for _ in range(n):
    a,b=map(int,input().split())
    x=max(a,b)
    y=a+b-x
    if(x%y==0):
        d=x//y
        s=bin(d)
        if(s.count('1')==1):
            print(cal(d))
        else:
            print(-1)
    else:
        print(-1)