t = int(input())
for i in range(t):
    n=int(input())
    s=0
    while(n>=10):
        k=n//10
        s=s+(k*10)
        n=n-(k*10)+k
    print(s+n)