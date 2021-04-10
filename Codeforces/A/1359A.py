t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    c=n//k
    if(c >= m):
        print(m)
    else:
        h = ((m-c)//(k-1))
        if((m-c)%(k-1) != 0):
            h+=1
        print(c-h)