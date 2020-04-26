t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    d = [0,0,0,0]
    c = 0
    for i in range(n):
        rem = arr[i]%4
        if rem>0:
            c+=d[4-rem]
        else:
            c+=d[0]
        d[rem] += 1
    print(c)
