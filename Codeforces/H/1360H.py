t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    m='1'*k
    x = int(m,2)
    a=list(range(0,x+1))
    for _ in range(n):
        s=input()
        h=(int(s,2))
        a.remove(h)
    l=len(a)
    if(l==0):
        print(-1)
    else:
        r = a[round((l-2)/2)]
        res = str(bin(r).replace("0b", ""))
        res = "0"*(k-len(res))+res
        print(res)