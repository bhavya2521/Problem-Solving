s=input()
if('0' in s):
    i=s.index('0')
    print(s[:i]+s[i+1:])
else:
    print(s[0:-1])