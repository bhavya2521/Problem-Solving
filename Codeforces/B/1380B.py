from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    st=input()
    n=len(st)
    r=0
    p=0
    s=0
    for i in st:
        if(i=="R"):
            r+=1
        elif(i=="S"):
            s+=1
        elif(i=="P"):
            p+=1
    m=max(r,p,s)
    n-=1
    if(m==r):
        res="P"*n
    elif(m==s):
        res="R"*n
    elif(m==p):
        res="S"*n
    print(res)