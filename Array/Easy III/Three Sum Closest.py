def threeSumClosest (arr, target):
    n = len(arr)
    if n<3:
        return -1
    arr.sort()
    diff = 2**31
    for i in range(n):
        l,r = i+1,n-1
        while l<r:
            s = arr[i]+arr[l]+arr[r]
            if abs(target-s)<abs(diff):
                diff = target-s
            if s<target:
                l+=1
            else:
                r-=1
        if diff==0:
            break
    return target-diff
