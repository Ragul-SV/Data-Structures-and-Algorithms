def isSafe(arr,n,i,j):
    return i>=0 and i<n and j>=0 and j<n and arr[i][j]==1
    
def solveMaze(arr,n,i,j,s,l,res):
    if i==n-1 and j==n-1 and arr[i][j]==1:
        s+=l
        res.append(s)
        
    if isSafe(arr,n,i,j):
        arr[i][j]=2
        s+=l
        solveMaze(arr,n,i+1,j,s,"D",res)
        solveMaze(arr,n,i,j-1,s,"L",res)
        solveMaze(arr,n,i,j+1,s,"R",res)
        solveMaze(arr,n,i-1,j,s,"U",res)
        arr[i][j] = 1

def findPath(arr, n):
    res = []
    s = ""
    l = ""
    solveMaze(arr,n,0,0,s,l,res)
    st = ""
    for i in res:
        st+=i+" "
    return st
