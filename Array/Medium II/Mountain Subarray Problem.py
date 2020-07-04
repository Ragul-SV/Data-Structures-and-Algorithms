def pre(arr,n,left,right):
    left[0] = 0
    lastInc = 0
    for i in range(1,n):
        if arr[i]>arr[i-1]:
            lastInc = i
        left[i] = lastInc
    right[n-1] = n-1
    firstdec = n-1
    for i in range(n-2,-1,-1):
        if arr[i]>arr[i+1]:
            firstdec = i
        right[i] = firstdec

def processqueries(arr,n,m,qu):
    left = [0]*n
    right = [0]*n
    pre(arr,n,left,right)
    res = []
    for q in qu:
        if right[q[0]]>=left[q[1]]:
            res.append("Yes")
        else:
            res.append("No")
    return res
