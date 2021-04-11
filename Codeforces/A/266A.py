n=int(input())
s=input()
res=""
j=0
for i in range(n):
    if(res=="" or res[j-1]!=s[i]):
        res+=s[i]
        j+=1
print(n-j)