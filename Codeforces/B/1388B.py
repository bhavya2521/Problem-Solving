from sys import*
input= stdin.readline
t=int(input())
p=[]
for _ in range(t):
    n=int(input())
    x=n//4
    if(n%4!=0):
        x+=1
    s="9"*(n-x)+"8"*x
    print(s)