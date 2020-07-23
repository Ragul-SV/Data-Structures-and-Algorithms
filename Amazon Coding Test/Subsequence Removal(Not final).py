from collections import OrderedDict
def findSubsequence(arr):
    d = OrderedDict()
    n = len(arr)
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]]+=1
    res = []
    for i in d:
        if d[i]>1:
            for j in range(d[i]-1):
                res.append(i)
    if res!=sorted(res):
        return [-1]
    return res
