row_index = [-1,-1,-1,0,0,1,1,1]
col_index = [-1,0,1,-1,1,-1,0,1]

def safe(arr,i,j,n,m,visited):
    return i>=0 and i<n and j>=0 and j<m and visited[i][j]==False and arr[i][j]==1

def dfs(arr,i,j,n,m,visited,temp):
    visited[i][j] = True
    for k in range(8):
        if safe(arr,i+row_index[k],j+col_index[k],n,m,visited):
            temp[0]+=1
            dfs(arr,i+row_index[k],j+col_index[k],n,m,visited,temp)
    
def findMaxArea(n,m,arr):
    visited = [[False for i in range(m)]for j in range(n)]
    res = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==False and arr[i][j]==1:
                temp = [1]
                dfs(arr,i,j,n,m,visited,temp)
                res = max(res,temp[0])
    return res
