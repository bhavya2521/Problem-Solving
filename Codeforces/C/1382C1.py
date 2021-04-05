from sys import*
input= stdin.readline
t=int(input())
def convert(a):
    x=""
    for i in a:
        if(i=="0"):
            x+="1"
        else:
            x+="0"
    return(x[::-1])
for _ in range(t):
    n=int(input())
    a=input()
    b=input()
    a=a.strip()
    b=b.strip()
    l=[]
    for i in range(n-1,-1,-1):
        c=0
        if(a[i]!=b[i]):
            if(b[i]==a[0]):
                c=1
                l.append(c)
                if(a[0]=="1"):
                    s="0"
                else:
                    s="1"
                a=s+a[1:]
                
                c=i+1
                l.append(c)
                s=convert(a[:i+1])
                a=s+a[i+1:]
            else:
                c=i+1
                l.append(c)
                s=convert(a[:i+1])
                a=s+a[i+1:]
    print(len(l),end=" ")
    for i in l:
        print(i,end=" ")
    print("")