from sys import*
input= stdin.readline
s=input()
if("AB" not in s or "BA" not in s):
    print("NO")
else:
    a=s.index("AB")
    b=s.rindex("AB")
    c=s.index("BA")
    d=s.rindex("BA")
    if(d-a > 1 or b-c >1):
        print("YES")
    else:
        print("NO")