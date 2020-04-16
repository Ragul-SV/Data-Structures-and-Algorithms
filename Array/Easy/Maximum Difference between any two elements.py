t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    maxDiff = -1
    min_so_far = arr[0]
    for i in range(1,n):
        maxDiff = max(maxDiff,arr[i]-min_so_far)
        min_so_far = min(min_so_far,arr[i])
    print(maxDiff)
