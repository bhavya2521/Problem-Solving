t=int(input())
for _ in range(t):
    n,x = map(int,input().split())
    l=list(map(int,input().split()))
    odd=0
    even=0
    for i in l:
        if(i%2==0):
            even+=1
        else:
            odd+=1
    if(x%2==0):
        if(even>=x//2 and odd>=x//2):
            print("Yes")
        else:
            print("No")
    else:
        if(odd >= x):
            print("Yes")
        else:
            print("No")