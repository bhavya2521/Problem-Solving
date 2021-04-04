import math
n,a,b,k = map(int,input().split())
l = list(map(int,input().split()))
p=0
track = 10**9
for i in range (n):
    r = l[i]%(a+b)
    if(r != 0):
        if(r <= a):
            p=p+1
        else:
            c = math.ceil(b/a)-1
            if(k>0 and k >= c and c <= track):
                k=k-c
                track = c
                p=p+1      
                
    if(r == 0):
        c = math.ceil(b/a)
        if(k>0 and k >= c and c <= track):
            k=k-c
            track = c
            p=p+1          
print(p)