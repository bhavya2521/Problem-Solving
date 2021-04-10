t=int(input())
for _ in range(t):
    n,m,x,y=map(int,input().split())
    s=0
    c=0
    for _ in range(n):
        l=input()
        c1=l.count('.')
        c2=l.count('..')
        s+=c2*y + (c1-2*c2)*x
        c+=c1
    print(min(s,c*x))