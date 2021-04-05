n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
s=0
for i in range(12):
    s+=l[i]
    if(s>=n):
        break
if(n==0):
    print(0)
elif(s>=n):
    print(i+1)
else:
    print(-1)