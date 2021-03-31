n=int(input())
for i in range(n+1):
    for j in range(n-i):
        print(" ",end=" ")
    r=""
    for k in range(i+1):
        r+=str(k)+" "
    if(i==0):
        print(r[:-1],end="")
    else:
        print(r,end="")
    r=r[::-1]
    print(r[3:])
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    r=""
    for k in range(n-i):
        r+=str(k)+" "
    if(i==n-1):
        print(r[:-1],end="")
    else:
        print(r,end="")
    r=r[::-1]
    print(r[3:])