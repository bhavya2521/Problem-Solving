import math
n=int(input())
res=0
for a in range(1,n,1):
    for b in range(1,n,1):
        c = math.sqrt(a*a+b*b)
        if(int(c)==c and c<=n):
            res+=1
print(res//2)