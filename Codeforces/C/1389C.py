from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    s=(input())
    s=s.strip()
    n=len(s)
    d={}
    for i in s:
        d[i]=d.get(i,0)+1
    l=list(d.values())
    k=list(d.keys())
    l.sort(reverse=True)
    if(l[0]==1):
        print(n-2)
    else:
        p=[]
        for i in range(len(k)):
            for j in range(i+1,len(k)):
                a=str(k[i])
                b=str(k[j])
                if(a!=b):
                    x=""
                    if(d.get(a)==1 or d.get(b)==1):
                        p.append(1)
                        continue
                    for h in s:
                        if(h==a or h==b):
                            x+=h
                    p.append(max(x.count(a+b),x.count(b+a)))
        if(p==[]):
            b=0
        else:
            b=max(p)*2
        print(min(n-l[0],n-b))