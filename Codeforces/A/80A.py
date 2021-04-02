l=[True]*51
p=2
while(p*p<50):
    if(l[p] == True):
        for i in range(p*p,51,p):
            l[i]=False
    p+=1
a,b=map(int,input().split())
if(l[a]==True and l[b]==True):
    if(True not in l[a+1:b]):
        print("YES")
    else:
        print("NO")
else:
    print("NO")