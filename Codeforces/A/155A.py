n=int(input())
l=list(map(int,input().split()))
max = l[0]
min = l[0]
c=0
for i in l:
    if(i>max):
        c+=1
        max=i
    elif(i<min):
        c+=1
        min=i
print(c)