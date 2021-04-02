from sys import*
input= stdin.readline
s=["S", "H", "D","C"]
r=["6", "7", "8", "9", "T", "J", "Q", "K", "A"]
t=input().strip()
a,b=map(str,input().split())
if(a[1]==t and b[1]!=t):
    print("YES")
elif(a[1]==b[1]):
    if(r.index(a[0])>r.index(b[0])):
        print("YES")
    else:
        print("NO")
else:
    print("NO")