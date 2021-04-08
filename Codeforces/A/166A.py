n,k=map(int,input().split())
p=[]
for _ in range(n):
    x,y = map(int,input().split())
    p.append([x,y])
p=sorted(p, key=lambda x: (-x[0], x[1]))
s=[0]
r=0
for i in range(n):
    if(p[i] not in p[:i]):
        r+=1
    s.append(r)
print(s.count(s[k]))