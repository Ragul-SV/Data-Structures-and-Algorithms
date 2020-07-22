def nextPermutation(n):
    arr = [int(x) for x in str(n)]
    n = len(arr)
    if n==1:
        return -1
    for i in range(n-1,0,-1):
        if arr[i]>arr[i-1]:
            break
    if i==1 and arr[i]<=arr[i-1]:
        return -1
    small = i
    for j in range(i+1,n):
        if arr[j]>arr[i-1] and arr[j]<arr[small]:
            small = j
    arr[i-1],arr[small] = arr[small],arr[i-1]
    res = int("".join(map(str,arr[:i]+sorted(arr[i:]))))
    if res > 2147483647:
        return -1
    return res
