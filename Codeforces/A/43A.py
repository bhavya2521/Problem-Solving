n=int(input())
d={}
for _ in range(n):
    a=input()
    d[a] = d.get(a,0)+1
print(max(d, key=d.get) )