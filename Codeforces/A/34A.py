n=int(input())
l=list(map(int,input().split()))
m=[]
for i in range(n-1):
    m.append(abs(l[i+1]-l[i]))
m.append(abs(l[0]-l[-1]))
i = m.index(min(m))
if(i==len(m)-1):
    print(n,1)
else:
    print(i+1,i+2)