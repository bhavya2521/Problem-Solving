n=int(input())
l=list(map(int,input().split()))
a=0
b=0
c=0
check=True
for i in l:
    if(i==25):
        a+=1
    elif(i==50 and a>=1):
        b+=1
        a-=1
    elif(i==100 and (a>=3 or (a>=1 and b>=1))):
        c+=1
        if(b>=1):
            b-=1
            a-=1
        else:
            a-=3
    else:
        print("NO")
        check=False
        break
if(check):
    print("YES")