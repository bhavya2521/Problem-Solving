n,k=map(int,input().split())
a=n//2
if(n%2!=0):
    a+= 1
if(k<=a):
    print(2*k-1)
else:
    print(2*(k-a))