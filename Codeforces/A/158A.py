n,k = map(int,input().split())
l=list(map(int,input().split()))
d = l[k-1]
c=k
if(d > 0):
    while(k<n):
        if(d == l[k]):
            c+=1
        else:
            break
        k+=1
    print(c)
else:
    c=0
    for i in l:
        if(i>0):
            c+=1
        else:
            break
    print(c)