n=int(input())
for i in range(n):
    x=int(input())
    if(x%2==0):
        print((x//2)-1)
    else:
        print(x//2)