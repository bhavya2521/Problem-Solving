from sys import*
input= stdin.readline
n=int(input())
c=0
for _ in range(n):
    i=int(input())
    if(i%2==0):
        print(i//2)
    else:
        if(c==0):
            print(i//2)
            c=1
        else:
            print((i//2)+1)
            c=0