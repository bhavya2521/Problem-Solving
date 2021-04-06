t=int(input())
for _ in range(t):
    n=int(input())
    m=[]
    l=[]
    for _ in range(n):
        l=input()
        m.append(l)
    c=0
    for i in range(n-1):
        for j in range(n-1):
            if(m[i][j]=='1'):
                if(m[i][j+1]=='0' and m[i+1][j]=='0'):
                    print("NO")
                    c=-1
                    break
        if(c==-1):
            break
    if(c==0):
        print("YES")