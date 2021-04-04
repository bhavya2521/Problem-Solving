from sys import*
input= stdin.readline
t=int(input())
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def fun(s,k):
    n=len(s)
    if(s==""):
        return 0
    elif(n==1):
        if(s!=alpha[k]):
            return 1
        else:
            return 0
    a=s[:n//2]
    b=s[n//2:]
    c1=a.count(alpha[k])
    c2=b.count(alpha[k])
    n=n//2
    if(c1<c2):
        return (n-c2)+  fun(a,k+1)
    elif(c1>c2):
        return (n-c1)+ fun(b,k+1)
    else:
        return(n-c1) + min(fun(a,k+1),fun(b,k+1))
for _ in range(t):
    n=int(input())
    s=input().strip()
    if(s=="a"):
        print(0)
    elif(n==1):
        print(1)
    else:
        print(fun(s,0))