n,t=map(int,input().split())
l=[]
for _ in range(t):
    x,y = map(int,input().split())
    l.append([x,y])
c=0
l.sort()
for i in range(t):
    if(n>l[i][0]):
        n+=l[i][1]
    else:
        print("NO")
        c=-1
        break
if(c==0):
    print("YES")