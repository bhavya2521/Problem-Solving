from sys import*
input= stdin.readline
l=[]
a=int(input())
b=int(input())
c=int(input())
x=a+b+c
y=(a+b)*c
z=a*b*c
d=a*(b+c)
print(max(x,y,z,d))