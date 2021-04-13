n=int(input())
b=[]
c=[]
for _ in range(n):
    x,y=map(int,input().split())
    b.append(x)
    c.append(y)
res=0
for i in range(n):
    if(b[i] in c[:i] or b[i] in c[i+1:]):
        res+=1
print(n-res)