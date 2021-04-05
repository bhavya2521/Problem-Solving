a=input()
b=input()
c=input()
x=[0]*26
z=[0]*26
for i in a:
    x[ord(i)-65]+=1
for i in b:
    x[ord(i)-65]+=1
for i in c:
    z[ord(i)-65]+=1
if(x==z):
    print("YES")
else:
    print("NO")