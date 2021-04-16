n,k = map(int,input().split())
s=input()
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l=[0]*k
for i in range(k):
    l[i] = s.count(alpha[i])
l.sort()
print(l[0]*k)