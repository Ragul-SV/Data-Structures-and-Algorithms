def minDist(arr, n, x, y):
    # Code here
    if x not in arr or y not in arr:
        return -1
    else:
        min_d = 2**31
        p = -1
        for i in range(n):
            if arr[i]==x or arr[i]==y:
                if p!=-1 and arr[i]!=arr[p]:
                    min_d = min(min_d,i-p)
                p = i
        return min_d
