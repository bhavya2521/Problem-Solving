t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    a=l[0]
    b=0
    x=l[0] # eaten by alice in one chance
    y=0 # eaten by bob in one chance
    i=1
    j=n-1
    c=1
    while(i<=j):
        y=0
        while(y<=x and i<=j):
            y+=l[j]
            b+=l[j]
            j-=1
        c+=1
        if(i>j):
            break
        x=0
        while(x<=y and i<=j):
            x+=l[i]
            a+=l[i]
            i+=1
        c+=1
    print(c,a,b)