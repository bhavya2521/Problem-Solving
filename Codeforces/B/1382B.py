from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    if(1 not in l or n==1):
        print("First")
    else:
        if(l[0]==1 and len(set(l))==1):
            if(n%2==0):
                print("Second")
            else:
                print("First")
        else:
            for i in range(n):
                if(l[i]!=1):
                    c=i+1
                    break
            if(c%2==0):
                print("Second")
            else:
                print("First")