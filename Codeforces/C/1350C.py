import math
n = int(input())
num=list(map(int,input().split()))
l=[]
for i in range(n):
    for j in range(i+1,n):
        g = math.gcd(num[i],num[j])
        l.append(num[i]*num[j]//g)
g = l[0]
for i in range(1,len(l)):
    g = math.gcd(g,l[i])
print(g)