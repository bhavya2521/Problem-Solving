n=int(input())
s=input()
ans=0
c=0
for i in s:
    if(i=='x'):
        c+=1
    else:
        ans+=max(c-2,0)
        c=0
if(c>2):
    ans+=c-2
print(ans)