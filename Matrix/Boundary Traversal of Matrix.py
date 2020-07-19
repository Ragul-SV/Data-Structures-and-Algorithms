def BoundaryTraversal(arr,m,n):
    k,l = 0,0
    for j in range(l,n):
        print(arr[k][j],end=" ")
    k+=1
    for i in range(k,m):
        print(arr[i][n-1],end=" ")
    n-=1
    if k<m:
        for j in range(n-1,l-1,-1):
            print(arr[m-1][j],end=" ")
        m-=1
    if l<n:
        for i in range(m-1,k-1,-1):
            print(arr[i][l],end=" ")
        l+=1
