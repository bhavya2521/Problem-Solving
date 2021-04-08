k=int(input())
l=[0]*26
s=input()
for i in s:
    l[ord(i)-97]+=1
r=""
c=0
for i in range(26):
    if(l[i]%k==0 and l[i]!=0):
        r+=chr(97+i)*(l[i]//k)
    elif(l[i]!=0):
        print(-1)
        c=-1
        break
if(c==0):
    print(r*k)