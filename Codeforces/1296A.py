t=int(input())
for _ in range(t):
    n = int(input())
    a = (list(map(int, input().split())))
    s=sum(a)
    if(s%2 != 0):
        print("YES")
    else:
            even = [num for num in a if num % 2 == 0] 
            c2 = len(even)
            c1 = n - c2
            if(c2 == n or (c1 == n and n%2 == 0)):
                print("NO")
            else:
                print("YES")