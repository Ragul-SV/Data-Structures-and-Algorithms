t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    count = 0
    for i in range(n):
        if arr[i]<=k:
            count+=1
    bad = 0
    for i in range(count):
        if arr[i]>k:
            bad+=1
    j = count
    res = bad
    for i in range(n):
        if j==n:
            break
        if arr[i]>k:
            bad-=1
        if arr[j]>k:
            bad+=1
        res = min(res,bad)
        j+=1
    print(res)
