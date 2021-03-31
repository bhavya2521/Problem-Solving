s=input()
l=['h','e','l','l','o']
j=0
for i in s:
    if(i==l[j]):
        j+=1
    if(j==5):
        break
if(j==5):
    print("YES")
else:
    print("NO")