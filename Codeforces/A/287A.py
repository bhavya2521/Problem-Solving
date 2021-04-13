l=[]
for _ in range(4):
    m=input()
    l.append(m)
c=0
for i in range(3):
    for j in range(3):
        m=[l[i][j],l[i][j+1],l[i+1][j],l[i+1][j+1]]
        a=m.count('#')
        if(a!=2):
            print("YES")
            c=-1
            break
    if(c==-1):
        break
if(c==0):
    print("NO")