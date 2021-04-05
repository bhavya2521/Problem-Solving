n=int(input())
l=list(map(int,input().split()))
s=sum(l)
if(n>s):
    n=n%s
m=0
if(n==0):
    for i in range(6,-1,-1):
        if(l[i]!=0):
            print(i+1)
            break
else:
    for i in range(7):
        m+=l[i]
        if(m>=n):
            print(i+1)
            break