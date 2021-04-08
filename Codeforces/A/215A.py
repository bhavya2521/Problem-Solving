n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
l=[]
for i in b:
    for j in a:
        if(i%j==0):
            l.append(i//j)
print(l.count(max(l)))