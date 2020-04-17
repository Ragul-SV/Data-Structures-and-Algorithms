t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int,input().strip().split()))
    arr = []
    for i in range(n):
        temp = []
        for j in range(i*n,i*n+n):
            temp.append(s[j])
        arr.append(temp)
    #Transpose Matrix
    for i in range(n):
        for j in range(i,n):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    #Reverse Rows
    for i in range(n):
        for j in range(n//2):
            arr[i][j],arr[i][n-1-j] = arr[i][n-1-j],arr[i][j]
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=" ")
    print()
