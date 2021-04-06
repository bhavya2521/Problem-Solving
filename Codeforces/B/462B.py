n,k=map(int,input().split())
l=input()
a=[0]*26
for i in l:
    a[ord(i)-65]+=1
a.sort(reverse=True)
c=0
s=0
i=0
while(c<k and i<n):
    x=min(k-c,a[i])
    c+=x
    s+=x*x
    i+=1
print(s)