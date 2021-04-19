import math
t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if(b>=a):
        print(b)
    else:
        if(c<=d):
            print(-1)
        else:
            print(int(b+c*math.ceil((a-b)/(c-d))))