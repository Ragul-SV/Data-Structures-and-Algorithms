t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = 0
    for i in range(32):
        count = 0
        for j in range(n):
            if arr[j] & (1<<i):
                count+=1
        res += count*(n-count)*2
    print(res)
