def maxSumPath(arr1, arr2, m, n):
    i,j = 0,0 
    s1 = 0
    s2 = 0
    res = 0
    while i<m and j<n:
        if arr1[i]==arr2[j]:
            res += max(s1,s2)
            s1 = 0
            s2 = 0
            while i<m and j<n and arr1[i]==arr2[j]:
                res+=arr1[i]
                i+=1
                j+=1
        elif arr1[i]<arr2[j]:
            s1+=arr1[i]
            i+=1
        elif arr2[j]<arr1[i]:
            s2+=arr2[j]
            j+=1
    while i<m:
        s1+=arr1[i]
        i+=1
    while j<n:
        s2+=arr2[j]
        j+=1
    res+=max(s1,s2)
    return res
