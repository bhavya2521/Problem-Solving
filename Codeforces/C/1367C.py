from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    s=input()
    s=s.strip()
    a=-1
    b=-1
    c=0
    for i in range(n):
        if(s[i]=="1" and a==-1):
            a=i
        elif(s[i]=="1" and b==-1):
            b=i
        if(b!=-1):
            c+=(b-a-1)//(k*2)
            a=b
            b=-1
    #print(c)
    if("1" in s):
        a=s.index("1")
        b=s[::-1].index("1")
        c+=a//(k+1)+b//(k+1)
    else:
        c=(n//(k+1))
        if(n<=k):
            c=1
    print(c)
    #print("")