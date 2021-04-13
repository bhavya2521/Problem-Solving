from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    s=input().strip()
    if(s=="2020" or s[:4]=="2020" or s[n-4:n]=="2020" or(s[0]=="2" and s[n-3:n]=="020") or (s[:2]=="20" and s[n-2:n]=="20") or (s[:3]=="202" and s[-1]=="0")):
        print("YES")
    else:
        print("NO")