t=int(input())
l=['1','0']
for _ in range(t):
    s=input()
    c=0
    for i in range(len(s)):
        if(s[i]=='0'):
            if('1' in s[:i] and '1' in s[i+1:]):
                c+=1
                s=s[:i]+l[int(s[i])]+s[i+1:]
        else:
            if('0' in s[:i] and '0' in s[i+1:]):
                c+=1
                s=s[:i]+l[int(s[i])]+s[i+1:]
    print(c)