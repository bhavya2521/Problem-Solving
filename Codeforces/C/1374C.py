t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    while("()" in s):
        s=s.replace("()","")
    print(len(s)//2)