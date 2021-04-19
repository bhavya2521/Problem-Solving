import math
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    m=k
    for _ in range(k):
        c=0
        if(n%2==0):
            n+=2*m
            break
        else:
            for i in range(3,int(math.sqrt(n))+1,2):
                if(n%i==0):
                    n+=i
                    c=1
                    m-=1
                    break   
        if(c==0):
            n+=n
            m-=1
    print(n)