from sys import*
input= stdin.readline
t=int(input())
for _ in range(t):
    s=input()
    l=[]
    c=0
    for i in range(len(s)):
        if(i==0 and s[i]=="1"):
            c+=1
        else:
            if(s[i]=="1" and s[i-1]=="1"):
                c+=1
            elif(s[i]=="1"):
                l.append(c)
                c=1
    l.append(c)
    l.sort(reverse=True)
    #print(l)
    c=0
    for i in range(len(l)):
        if(i%2==0):
            c+=l[i]
    print(c)