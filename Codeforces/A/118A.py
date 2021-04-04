s=input()
s=s.lower()
l=['a','e','i','o','u','y']
r=""
for i in s:
    if(i not in l):
        r+="."+i
print(r)