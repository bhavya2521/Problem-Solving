t=int(input())
for _ in range(t):
    n=(input())
    l=len(n)
    c=0
    p=[]
    for i in range(l):
        r=int(n[i])*(10**(l-1-i))
        if(r!=0):
            c+=1
            p.append(r)
    print(c)
    for i in p:
        print(i,end=" ")
    print("")