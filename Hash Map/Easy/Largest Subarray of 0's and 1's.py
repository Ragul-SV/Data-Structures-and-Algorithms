def maxLen(arr):
    d = dict()
    maxlen = 0
    s = 0
    d[0] = -1
    for i in range(len(arr)):
        if arr[i]==0:
            s-=1
        elif arr[i]==1:
            s+=1
        if s not in d:
            d[s] = i
        else:
            maxlen = max(maxlen,i-d[s])
    return maxlen
