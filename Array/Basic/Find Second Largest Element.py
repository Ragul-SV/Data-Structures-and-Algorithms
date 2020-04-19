t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    maxA = max(arr[0],arr[1])
    maxB = min(arr[0],arr[1])
    if maxA==maxB:
        maxB = -1
    for i in range(2,n):
        if arr[i]>maxA:
            maxB = maxA
            maxA = arr[i]
        elif arr[i]>maxB and arr[i]!=maxA:
            maxB = arr[i]
    print(maxB)
