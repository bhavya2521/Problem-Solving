from sys import*
input= stdin.readline
n=int(input())
l=[1]
for i in range(1,5):
    x=10**i
    j=len(l)
    l.append(x)
    for i in range(j):
        l.append(x+l[i])
l.append(10**6)
if(n<10):
    print(n)
    for _ in range(n):
        print(1,end=" ")
    print("")
else:
    p=[]
    if(n==10**6):
        print(1)
        print(10**6)
    else:
        while(n!=0):
            for i in range(31):
                if(n>=l[i] and n<l[i+1]):
                    p.append(l[i])
                    n-=l[i]
        print(len(p))
        for i in p:
            print(i,end=" ")