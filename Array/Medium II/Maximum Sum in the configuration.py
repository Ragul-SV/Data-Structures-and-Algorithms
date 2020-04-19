def max_sum(a,n):
    s = a[0]
    max_sum = 0
    for i in range(1,n):
        s += a[i]
        max_sum += i*a[i]
    res = max_sum
    for i in range(1,n):
        max_sum = max_sum-(s-a[i-1])+a[i-1]*(n-1) 
        res = max(res,max_sum)
    return res
