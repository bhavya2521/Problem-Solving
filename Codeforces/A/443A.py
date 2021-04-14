from sys import*
input= stdin.readline
s=input()
res=set()
for i in s:
    if(96 < ord(i) < 123):
        res.add(i)
print(len(res))