def isPangram(arr):
    res = ""
    for i in range(len(arr)):
        d = dict()
        s = arr[i]
        for j in range(len(s)):
            if s[j]!=' ':
                if s[j] not in d:
                    d[s[j]] = 1
                else:
                    d[s[j]]+=1
        flag = 1
        for j in range(97,123):
            if chr(j) not in d:
                res+='0'
                flag = 0
                break
        if flag:
            res+='1'
    print(d)
    return res
