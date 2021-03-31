n=int(input())
l=list(map(int,input().split()))
l.sort()
k=0
for i in range(n):
    k+=abs(l[i]-(i+1))
print(k)