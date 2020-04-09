def pythagoreas(arr,n):
    d = dict()
    for i in range(n):
        arr[i] = arr[i]*arr[i]
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = i
    for i in range(n-1):
        for j in range(i+1,n):
            if (arr[i]+arr[j]) in d:
                return "Yes"
    return "No"

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    print(pythagoreas(arr,n))
