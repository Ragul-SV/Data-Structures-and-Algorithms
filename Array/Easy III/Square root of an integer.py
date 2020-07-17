def floorSqrt(x): 
    if x==1:
        return x
    st,end = 1,x
    while st<=end:
        mid = (st+end)//2
        if (mid*mid)==x:
            return mid
        if (mid*mid)<x:
            st = mid+1
            res = mid
        else:
            end = mid-1
    return res
