q=int(input())
for _ in range(q):
    n=int(input())
    l=[]
    for _ in range(n):
        t = list(map(int,input().split()))
        l.append(t)
    l.sort()
    c=0
    s=""
    l.insert(0,[0,0])
    for i in range(n):
        if(l[i][1] > l[i+1][1]):
            print("NO")
            c=-1
            break
        else:
            x = l[i+1][0]-l[i][0]
            y = l[i+1][1]-l[i][1]
            s+='R'*x+'U'*y
    if(c==0):
        print("YES")
        print(s)