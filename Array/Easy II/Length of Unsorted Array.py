def unsorted_subarray(arr,n):
    s,e = 0,0
    for s in range(n-1):
        if arr[s]>arr[s+1]:
            break
    if s==n-1:
        return 0,0
    e = n-1
    while e>0:
        if arr[e]<arr[e-1]:
            break
        e-=1
    min_s = min(arr[s:e+1])
    max_s = max(arr[s:e+1])
    for i in range(s):
        if arr[i]>min_s:
            s = i
            break
    i = n-1
    while i>=e+1:
        if arr[i]<max_s:
            e = i
            break
        i-=1
    return s,e
    
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s,e = unsorted_subarray(arr,n)
    print(s,e)
