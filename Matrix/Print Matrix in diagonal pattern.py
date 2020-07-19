def printMatrixDiagonal(arr, n):
    i,j,k = 0,0,0
    isUp = True
    while k<n*n:
        if isUp:
            while i>=0 and j<n:
                print(arr[i][j],end=" ")
                i-=1
                j+=1
                k+=1
            if i<0 and j<n:
                i = 0
            if j==n:
                j-=1
                i+=2
        else:
            while i<n and j>=0:
                print(arr[i][j],end=" ")
                i+=1
                j-=1
                k+=1
            if i==n:
                i-=1
                j+=2
            if j<0 and i<n:
                j = 0
        isUp = not isUp
