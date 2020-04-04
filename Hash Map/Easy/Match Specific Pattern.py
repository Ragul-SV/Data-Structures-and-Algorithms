from collections import OrderedDict
def findSpecificPattern(n, arr, string):
    d = OrderedDict()
    for i in range(len(string)):
        if string[i] not in d:
            d[string[i]] = 1
        else:
            d[string[i]] += 1
    l = list(d.values())
    res = []
    for i in range(len(arr)):
        d.clear()
        for j in range(len(arr[i])):
            if arr[i][j] not in d:
                d[arr[i][j]] = 1
            else:
                d[arr[i][j]] += 1
        if l==list(d.values()):
            res.append(arr[i])
    return res
