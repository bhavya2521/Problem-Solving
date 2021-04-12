l=[]
def add(i,j):
    res=l[i][j]
    m=[[i,j-1],[i-1,j],[i,j+1],[i+1,j]]
    for k in m:
        if((0<= k[0] <3) and (0<= k[1] <3)):
            res+=l[k[0]][k[1]]
    return res
for _ in range(3):
    m=list(map(int,input().split()))
    l.append(m)
for i in range(3):
    for j in range(3):
        if((add(i,j))%2!=0):
            print(0,end="")
        else:
            print(1,end="")
    print("")