from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    p=[]
    i=0
    j=n-1
    k=0
    while(i<n and j>=i):
        x=min(l[i],l[j])
        if(p==[]):
            p.append(x)
            if(x==l[i]):
                i+=1
            else:
                j-=1
        else:
            y=p[-1]
            if(y<=x):
                p.append(x)
                if(x==l[i]):
                    i+=1
                else:
                    j-=1
            else:
                p=[]
                j=n-1
                if(x!=l[i]):
                    i+=1
    print(n-len(p))