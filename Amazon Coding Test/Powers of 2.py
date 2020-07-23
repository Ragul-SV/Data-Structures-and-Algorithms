import math
def isPower(arr):
    res = []
    for i in range(len(arr)):
        if arr[i]!=0 and math.log(arr[i],2).is_integer():
            res.append(1)
        else:
            res.append(0)
    return res
