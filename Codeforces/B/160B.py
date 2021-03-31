n=int(input())
s=input()
c1=0
c2=0
a=list(s[:n])
b=list(s[n:])
a.sort()
b.sort()
for i in range(n):
    if(a[i]>b[i]):
        c1+=1
    elif(a[i]<b[i]):
        c2+=1
if(c1==n or c2==n):
    print("YES")
else:
    print("NO")