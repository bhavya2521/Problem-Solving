for _ in range(int(input())):
    n,x,y= [int(a) for a in input().split()] 
    if(n==1):
        print("YES")
    else:
        l1=input().split()
        l2=input().split()
        if(max(l1)>max(l2)):
            print("YES")
        else:
            print("NO")