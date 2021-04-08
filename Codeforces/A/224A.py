import math
x,y,z=map(int,input().split())
a=math.sqrt(x*z/y)
b=math.sqrt(x*y/z)
c=math.sqrt(y*z/x)
print(int(4*(a+b+c)))