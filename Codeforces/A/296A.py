n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i] = d.get(i,0)+1
x=d.values()
p=n//2
if(n%2!=0):
    p+=1
if(max(x)<=p):
    print("YES")
else:
    print("NO")