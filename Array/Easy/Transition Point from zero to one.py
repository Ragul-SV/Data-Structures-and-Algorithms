def transitionPoint(arr, n):
    l = 0
    r = n-1
    while l<=r:
        mid = (l+r)//2
        if (mid==0 or mid==n-1) and arr[mid]==0:
            return -1
        elif (mid==0 or mid==n-1) and arr[mid]==1:
            return mid
        if arr[mid-1]==0 and arr[mid]==1:
            return mid
        if arr[mid]==0:
            l = mid+1
        elif arr[mid]==1:
            r = mid-1
    return mid
