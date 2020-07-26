def ways(arr,n):
    arr.sort()
    res = set()
    for i in range(n-2):
        if arr[i]>0:
            break
        l,r = i+1,n-1
        while l<r:
            temp = arr[i] + arr[l] + arr[r]
            if temp>0:
                r-=1
            elif temp<0:
                l+=1
            else:
                res.add(tuple([arr[i],arr[l],arr[r]]))
                l+=1
                r-=1
    return len(res) 
