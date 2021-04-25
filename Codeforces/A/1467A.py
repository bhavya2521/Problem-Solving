from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    t="9876543210"
    ans=""
    x=n//10
    y=n%10
    ans=t*x+t[:y]
    print(ans)