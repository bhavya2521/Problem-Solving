n=int(input())
def check(n):
    l=[]
    s=str(n)
    for i in range(4):
        if(s[i] in l):
            return False
        l.append(s[i])
    return True
while(True):
    n=n+1
    if(check(n)):
        break
print(n)