n=int(input())
c=0
for _ in range(n):
    l=list(map(int,input().split()))
    if(l.count(1)>=2):
        c+=1
print(c)