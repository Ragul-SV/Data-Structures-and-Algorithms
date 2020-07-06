def maxArea(arr,n):
    l,r = 0,n-1
    res = 0
    while l<r:
        res = max(res,min(arr[l],arr[r])*(r-l))
        if arr[l]<arr[r]:
            l+=1
        else:
            r-=1
    return res
