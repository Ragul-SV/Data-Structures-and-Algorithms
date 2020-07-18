def point(arr,n):
    l,r = 0,n-1
    while l<=r:
        mid = (l+r)//2
        if mid<r and arr[mid]>arr[mid+1]:
            return mid+1
        if mid>l and arr[mid]<arr[mid-1]:
            return mid
        elif arr[mid]>arr[l]:
            l = mid+1
        else:
            r = mid-1
    return -1
    
def binarysearch(arr,l,r,k):
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]<k:
            l = mid+1
        else:
            r = mid-1
    return -1
            
def Search(arr,n,k):
    p = point(arr,n)
    if p==-1:
        return binarysearch(arr,0,n-1,k)
    
    if arr[p]==k:
        return p
    if arr[0]<=k:
        return binarysearch(arr,0,p-1,k)
    else:
        return binarysearch(arr,p+1,n-1,k)
