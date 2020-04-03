def maxLen(n, arr):
    d = dict()
    s = 0
    maxlen = 0
    d[0] = -1
    for i in range(n):
        s += arr[i]
        if s not in d:
            d[s] = i
        else:
            maxlen = max(maxlen,i-d[s])
    return maxlen
