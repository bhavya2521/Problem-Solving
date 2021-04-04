n=int(input())
l=list(map(int,input().split()))
s=set(l)
res=[]
for i in s:
    k=[index for index, value in enumerate(l) if value == i]
    if(len(k)==1):
        res.append([i,0])
        continue
    else:
        d=k[1]-k[0]
        c=0
        for j in range(len(k)-1):
            if(k[j+1]-d != k[j]):
                c=-1
                break
        if(c==0):
            res.append([i,d])
print(len(res))
res.sort()
for i in res:
    print(i[0],i[1])