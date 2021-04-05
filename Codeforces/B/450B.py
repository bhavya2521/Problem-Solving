x,y = map(int,input().split())
n=int(input())
n=n%6
M=1000000007
l=[x-y,x,y,y-x,-x,-y]
print(l[n]%M)