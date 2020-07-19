def findK(arr, m, n, q):
    k,l = 0,0
    c = 0
    while k<m and l<n:
        for j in range(l,n):
            c+=1
            if c==q:
                return arr[k][j]
        k+=1
        for i in range(k,m):
            c+=1
            if c==q:
                return arr[i][n-1]
        n-=1
        if k<m:
            for j in range(n-1,l-1,-1):
                c+=1
                if c==q:
                    return arr[m-1][j]
            m-=1
        if l<n:
            for i in range(m-1,k-1,-1):
                c+=1
                if c==q:
                    return arr[i][l]
            l+=1
