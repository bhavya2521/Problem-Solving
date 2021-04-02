n=int(input())
max=0
m=0
for _ in range(n):
    a,b=map(int,input().split())
    m+=b-a
    if(m>max):
        max=m
print(max)