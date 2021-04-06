n=int(input())
l=list(map(int,input().split()))
a=max(l)
b=min(l)
if(a!=b):
    print(a-b,l.count(a)*l.count(b))
else:
    print(0,(n-1)*(n)//2)