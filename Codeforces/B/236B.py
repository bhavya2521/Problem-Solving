a,b,c=map(int,input().split())
M=1073741824
n=a*b*c
d=[1]*(n+1)
for i in range(2,n+1):
	for j in range(i,n+1,i):
	    d[j]+=1
r=0
for i in range(1,a+1):
	for j in range(1,b+1):
		for k in range(1,c+1):
			r+=(d[i*j*k])%M
print(r%M)