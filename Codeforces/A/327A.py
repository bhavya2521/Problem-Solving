from sys import*
input= stdin.readline
n=int(input())
l=list(map(int,input().split()))
if(0 not in l):
    print(n-1)
else:
    i=l.index(0)
    j=n-1-l[::-1].index(0)
    c=n-(j-i+1)
    if(1 not in l[i:j+1]):
        print(n)
    else:
        r=0
        for k in range(i,j+1):
            r=max(r,l[i:k+1].count(0))
        print(r+c)