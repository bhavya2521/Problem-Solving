from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,c0,c1,h=map(int,input().split())
    s=input()
    if(c0==c1):
        print(n*c0)
        continue
    a,b=0,0
    for i in s.strip():
        if(i=='0'):
            a+=1
        else:
            b+=1
    #print(a,b)
    if(h>=max(c0,c1)):
        print(a*c0 + b*c1)
    else:
        if(c0>c1+h):
            print(a*h + n*c1)
        elif(c1>c0+h):
            print(b*h + n*c0)
        else:
            print(a*c0 + b*c1)