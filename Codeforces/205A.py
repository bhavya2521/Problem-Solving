n=int(input())
l=list(map(int,input().split()))
m=min(l)
if(l.count(m)>1):
    print("Still Rozdil")
else:
    print(l.index(m)+1)