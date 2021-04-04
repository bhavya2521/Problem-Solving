l=[4,7,47,74,444,777,447,477,744,774,474,747]
n=int(input())
if(n in l):
    print("YES")
else:
    c=0
    for i in l:
        if(n%i == 0):
            c=1
            break
    if(c==1):
        print("YES")
    else:
        print("NO")