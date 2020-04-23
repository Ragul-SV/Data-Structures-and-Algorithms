def maxSumPath(arr1, arr2, m, n):
    i,j = 0,0 
    s1 = 0
    s2 = 0
    res = 0
    while i<m and j<n:
        if arr1[i]==arr2[j]:
            res += max(s1,s2)+arr1[i]
            s1 = 0
            s2 = 0
        else:
            s1+=arr1[i]
            s2+=arr2[j]
        i+=1
        j+=1
        if i==m and j==n:
            res+=max(s1,s2)
        elif i==m:
            temp = s2
            while j<n:
                temp+=arr2[j]
                j+=1
            res+=max(s1,temp)
        elif j==n:
            temp = s1
            while i<m:
                temp+=arr1[i]
                i+=1
            res+=max(s2,temp)
        print(i,res)
    return res
