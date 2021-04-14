n=int(input())
l=list(map(int,input().split()))
a=l.count(5)
s=""
if(a==0):
    print(0)
else:
    if(a>=9 and n-a>=1):
        s+='5'*((a//9)*9)+'0'*(n-a)
        print(s)
    else:
        if(0 in l):
            print(0)
        else:
            print(-1)