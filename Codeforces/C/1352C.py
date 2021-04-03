t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    k = k + k//(n-1)
    if(k%n==0):
        k-=1
    print(k)