n=int(input())
l=list(map(int,input().split()))
s=sum(l)
m=[1,2,3,4,5]
c=0
for i in m:
    if((s+i)%(n+1)!=1):
        c+=1
print(c)