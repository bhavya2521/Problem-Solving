q=int(input())
for _ in range(q):
    a,b,c,n= map(int,input().split())
    s = a+b+c
    m = max(a,b,c)
    x = 3*m-s
    if(n>=x and (n-x)%3 == 0 ):
        print("YES")
    else:
        print("NO")