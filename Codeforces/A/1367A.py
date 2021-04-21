l=int(input())
for _ in range(l):
    s=input()
    n=len(s)
    a=s[1:n]
    r=""
    i=1
    while(i<n-1):
        r+=a[i]
        i+=2
    print(s[0]+r+s[-1])