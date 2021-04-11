a,b,n= map(int,input().split())
c=0
r=str(a)
d=len(r)
for i in range(n):
    s=b-(a*10)%b
    if(s>9 and s!=b):
        print(-1)
        c=-1
        break
    elif(s==b):
        a=a*10+0
        t="0"*(n+d-len(r))
        r+=t
        break
    else:
        a=a*10+s
        r+=str(s)
if(c==0):
    print(r)