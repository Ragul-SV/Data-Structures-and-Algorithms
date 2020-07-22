import sys
sys.setrecursionlimit(100000)
row_index = [-1,-1,-1,0,0,1,1,1]
col_index = [-1,0,1,-1,1,-1,0,1]
def Safe(arr,i,j,m,n,visited):
    return i>=0 and i<m and j>=0 and j<n and (not visited[i][j]) and arr[i][j]==1
    
def DFS(arr,i,j,m,n,visited):
    visited[i][j] = True
    for k in range(8):
        if Safe(arr,i+row_index[k],j+col_index[k],m,n,visited):
            DFS(arr,i+row_index[k],j+col_index[k],m,n,visited)
    
def findIslands(arr, m, n):
    visited = [[False for j in range(n)]for i in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            if visited[i][j]==False and arr[i][j]==1:
                DFS(arr,i,j,m,n,visited)
                res+=1
    return res
