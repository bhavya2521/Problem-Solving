t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    even=0
    odd=0
    m=[]
    for i in l:
        if(i%2==0):
            even+=1
        else:
            odd+=1
        if(i-1 in l or i+1 in l):
            m.append(i)
    if(even%2 == 0 and odd%2==0):
        print("YES")
    else:
        m=list(set(m))
        k=len(m)
        c=0
        while(k>0):
            k=k-2
            even-=1
            odd-=1
            if(even%2 == 0 and odd%2==0):
                print("YES")
                c=-1
                break
        if(c==0):
            print("NO")