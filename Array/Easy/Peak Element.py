def peakElement(arr, n):
    l = 0
    r = n-1
    res = 0
    while l<=r:
        mid = (l+r)//2
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==n-1 or arr[mid+1]<=arr[mid]):
            res = mid
            break
        elif mid>0 and arr[mid-1]>arr[mid]:
            r = mid-1
        elif mid<n-1 and arr[mid+1]>arr[mid]:
            l = mid+1
    print(arr[res])
    return res
