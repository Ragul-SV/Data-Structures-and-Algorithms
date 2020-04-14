def minHeight(arr,n,k):
    if n==1:
        return 0
    res = arr[n-1]-arr[0]
    small = arr[0]+k
    big = arr[n-1]-k
    if big<small:
        small,big = big,small
    for i in range(1,n-1):
        subtract = arr[i]-k
        add = arr[i]+k
        if subtract>=small or add<=big:
            continue
        if big-subtract<=add-small:
            small = subtract
        else:
            big = add
    return min(res,big-small)

t = int(input())
for cases in range(t):
    k = int(input())
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    print(minHeight(arr,n,k))
