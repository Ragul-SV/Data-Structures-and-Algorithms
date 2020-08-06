def strength(grid,n,m):
    arr = []
    for i in range(n+5):
        arr.append([-2**31]*(m+5))
    for i in range(n):
        for j in range(m):
            arr[i+1][j+1] = grid[i][j]
    for i in range(2,n+1):
        for j in range(1,m+1):
            arr[i][j] += max(arr[i-1][j-1],arr[i-1][j],arr[i-1][j+1])
    res = -1
    for j in range(1,m+1):
        res = max(res,arr[n][j])
    return max(0,res)
