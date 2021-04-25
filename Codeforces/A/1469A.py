from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    s=input().strip()
    n=len(s)
    if(n%2!=0):
        print("NO")
        continue
    a,b,c=0,0,0
    for i in s:
        if(i=="("):
            a+=1
        elif(i==")"):
            b+=1
        else:
            c+=1
        if(a<b):
            if(c!=0):
                a=b
                c-=1
            else:
                c=1
                break
    if(c%2==0):
        print("YES")
    else:
        print("NO")