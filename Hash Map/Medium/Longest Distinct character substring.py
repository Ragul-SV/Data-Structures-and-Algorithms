def longestUniqueSubstr(arr):
    s = set()
    n = len(arr)
    st,end=0,0
    temp = []
    maxlen = 0
    res = ""
    while end<n:
        if arr[end] not in s:
            s.add(arr[end])
            temp.append(arr[end])
        else:
            temp.append(arr[end])
            while arr[st]!=arr[end]:
                temp.pop(0)
                s.remove(arr[st])
                st+=1
            temp.pop(0)
            st+=1
        end+=1
        if maxlen<end-st:
            maxlen = end-st
            res = "".join(temp)
    return maxlen
