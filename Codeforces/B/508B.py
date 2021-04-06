from sys import*
input= stdin.readline
s=input().strip()
n=len(s)
a=[]
b=[]
for i in range(n):
    x=int(s[i])
    if(x%2==0):
        a.append(i)
        b.append(x)
if(a==[]):
    print(-1)
else:
    m=min(b)
    if(m>int(s[-1])):
        x=a[-1]
    elif(m<int(s[-1])):
        x=a[b.index(m)]
    r=s[:x]+s[-1]+s[x+1:n-1]+s[x]
    print(r)