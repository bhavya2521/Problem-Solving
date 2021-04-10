t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = n*m
    c = a//2
    if(a%2!=0):
        c+=1
    print(c)