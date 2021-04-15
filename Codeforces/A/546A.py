k,m,n = map(int,input().split())
t = (n*(n+1)//2)*k
if(t<=m):
    print(0)
else:
    print(t-m)