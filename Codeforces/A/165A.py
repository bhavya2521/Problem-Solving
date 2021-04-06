n=int(input())
l=[]
for _ in range(n):
    m=list(map(int,input().split()))
    l.append(m)
l.sort()
c=0
for i in range(1,n-1):
    m=[False,False,False,False]
    for j in range(i-1,-1,-1):
        if(l[i][0]-l[j][0] == 0 and l[i][1]-l[j][1]>0):
            m[0]=True
        elif(l[i][1]-l[j][1] == 0 and l[i][0]-l[j][0]>0):
            m[1]=True
    for j in range(i+1,n):
        if(l[i][0]-l[j][0] == 0 and l[i][1]-l[j][1]<0):
            m[2]=True
        elif(l[i][1]-l[j][1] == 0 and l[i][0]-l[j][0]<0):
            m[3]=True
    if(False not in m):
        c+=1
print(c)