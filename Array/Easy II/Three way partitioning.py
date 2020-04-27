def threeWayPartition(arr, n, a, b):
    l,mid,r = 0,0,n-1
    while mid<=r:
        if arr[mid]<a:
            arr[l],arr[mid] = arr[mid],arr[l]
            l+=1
            mid+=1
        elif arr[mid]>=a and arr[mid]<=b:
            mid+=1
        else:
            arr[mid],arr[r] = arr[r],arr[mid]
            r-=1
    return arr
