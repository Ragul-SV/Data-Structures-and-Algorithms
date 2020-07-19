def search(m, n, arr, x):
    i,j = 0,n-1
    while i<m and j>=0:
        if arr[i][j]==x:
            return 1
        if x<arr[i][j]:
            j-=1
        else:
            i+=1
    return 0
