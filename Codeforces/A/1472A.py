from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    w,h,n=map(int,input().split())
    a,b=0,0
    while(w%2==0 and w!=0):
        w=w//2
        a+=1
    while(h%2==0 and h!=0):
        h=h//2
        b+=1
    c=2**(a+b)
    if(c>=n):
        print("YES")
    else:
        print("NO")