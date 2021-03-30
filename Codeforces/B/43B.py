h=input()
l=input()
a=[0]*26
b=[0]*26
c=[0]*26
d=[0]*26
for i in h:
    if(i.islower()):
        a[ord(i)-97]+=1
    elif(i.isupper()):
        b[ord(i)-65]+=1
for i in l:
    if(i.islower()):
        c[ord(i)-97]+=1
    elif(i.isupper()):
        d[ord(i)-65]+=1
res=0
for i in range(26):
    if((c[i]!=0 and c[i]>a[i]) or (d[i]!=0 and d[i]>b[i]) ): 
            res=-1
            print("NO")
            break
if(res==0):
    print("YES")