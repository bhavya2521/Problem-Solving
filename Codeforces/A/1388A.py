from sys import*
input= stdin.readline
t=int(input())
p=[]
for _ in range(t):
    n=int(input())
    if(n<31):
        print("NO")
    else:
        print("YES")
        if(n==36):
            print(5,6,10,15)
        elif(n==40):
            print(6,14,15,5)
        elif(n==44):
            print(6,7,10,21)
        else:
            print(6,10,14,n-30)