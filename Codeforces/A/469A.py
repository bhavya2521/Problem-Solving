from sys import*
input= stdin.readline
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a=a[1:]
b=b[1:]
a.extend(b)
s=list(set(a))
if(len(s)-s.count(0)!=n):
    print("Oh, my keyboard!")
else:
    print("I become the guy.")