n,a,b,c,d=map(int,input().split())
s=input()
r=0
check=True
north = False
east = False
west = False
south =False
if(d>b):
    north = True
if(b>d):
    south = True
if(c>a):
    east =True
if(a>c):
    west = True
for i in s:
    if(i=="S"and south and b!=d):
        b-=1
    elif(i=="N" and north and b!=d):
        b+=1
    elif(i=="E" and east and a!=c):
        a+=1
    elif(i=="W" and west and a!=c):
        a-=1
    r+=1
    if(a==c and b==d):
        print(r)
        check=False
        break
if(check):
    print(-1)