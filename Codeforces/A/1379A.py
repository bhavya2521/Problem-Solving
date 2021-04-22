from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    a="abacaba"
    s=s.strip()
    if(s==""):
        continue
    if(a in s):
        c=0
        for i in range(n):
            d=s[i:i+7]
            if(d==a):
                c+=1
        if(c==1):
            print("Yes")
            s=s.replace("?",'z')
            print(s.strip())
        else:
            print("No")
    else:
        for i in range(0,n):
            d=s[i:i+7]
            if(len(d)!=7):
                break
            x=0
            for j in range(7):
                if(d[j]!=a[j] and d[j]!="?"):
                    x=-1
                    break
                elif(d[j]=="?"):
                    d=d[:j]+a[j]+d[j+1:]
            if(x==0):
                g=s[:i]+d+s[i+7:]
                c=0
                for i in range(0,n):
                    d=g[i:i+7]
                    if(d==a):
                        c+=1
                if(c==1):
                    print("Yes")
                    g=g.replace("?",'z')
                    print(g.strip())
                    break
                else:
                    x=-1
        if(x==-1):
            print("No")