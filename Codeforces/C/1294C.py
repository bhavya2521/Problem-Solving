import math
q=int(input())
for _ in range(q):
    n=int(input())
    divisor = [] 
    for i in range(2, n + 1): 
        while (n % i == 0): 
            divisor.append(i) 
            n //= i 
    if (n != 1): 
        divisor.append(n) 
    a, b, c, size = 0, 0, 0, 0
    a = b = c = 1
    size = len(divisor) 
    for i in range(size): 
        if (a == 1): 
            a = a * divisor[i] 
        elif (b == 1 or b == a): 
            b = b * divisor[i] 
        else: 
            c = c * divisor[i] 
    if (a == 1 or b == 1 or c == 1 or a == b or b == c or a == c): 
        print("NO") 
    else: 
        print("YES")
        print(a,b,c)