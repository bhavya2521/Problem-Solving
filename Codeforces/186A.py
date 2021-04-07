a=input()
b=input()
x=[0]*26
y=[0]*26
n=len(a)
m=len(b)
c=0
if(n==m):
    for i in range(n):
        x[ord(a[i])-97]+=1
        y[ord(b[i])-97]+=1
    if(x==y):
        for i in range(n):
            if(a[i]!=b[i]):
                c+=1
            if(c>2):
                print("NO")
                break
        if(c==2 or (c==0 and len(a)!=len(set(a)))):
            print("YES")
        elif(c<2):
            print("NO")
    else:
        print("NO")
else:
    print("NO")