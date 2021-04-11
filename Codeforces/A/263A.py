for i in range(5):
    l=input().split()
    if('1' in l):
        k=l.index('1')
        print(abs(3-k-1)+abs(3-i-1))