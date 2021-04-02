a=0
b=0
c=0
n=int(input())
for _ in range(n):
    l=list(map(int, input().split()))
    a=a+l[0]
    b=b+l[1]
    c=c+l[2]
if(a==0 and b==0 and c==0):
    print("YES")
else:
    print("NO")