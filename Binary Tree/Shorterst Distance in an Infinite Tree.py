t = int(input())
for cases in range(t):
    x,y = map(int,input().strip().split())
    c = 0
    while x!=y:
        if x>y:
            x = x//2
        else:
            y = y//2
        c+=1
    print(c)
