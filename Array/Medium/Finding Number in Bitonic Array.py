def ascendingBinarySearch(arr,l,r,key):
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1
    
def descendingBinarySearch(arr,l,r,key):
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==key:
            return mid
        elif key<arr[mid]:
            l = mid+1
        else:
            r = mid-1
    return -1
            
def bitonicPoint(arr,n,l,r):
    while 1:
        mid = (l+r)//2
        if mid==0 or mid==n-1:
            return -1
        if arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid-1]<arr[mid] and arr[mid]<arr[mid+1]:
            l = mid+1
        elif arr[mid-1]>arr[mid] and arr[mid]>arr[mid+1]:
            r = mid-1
    return -1
    
def searchBitonic(arr,n,index,key):
    if index==-1:
        res = ascendingBinarySearch(arr,0,n-1,key)
        if res!=-1:
            return res
        return descendingBinarySearch(arr,0,n-1,key)
    if key>arr[index]:
        return -1
    else:
        if arr[index]==key:
            return index
        else:
            res = ascendingBinarySearch(arr,0,index-1,key)
            if res!=-1:
                return res
            return descendingBinarySearch(arr,index+1,n-1,key)

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    key = int(input())
    index = bitonicPoint(arr,n,0,n-1) 
    print(searchBitonic(arr,n,index,key))
