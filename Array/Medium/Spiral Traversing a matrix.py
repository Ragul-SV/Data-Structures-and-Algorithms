t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    matrix = list(map(int,input().strip().split()))
    arr = []
    for i in range(m):
        b = []
        for j in range(i*n,i*n+n):
            b.append(matrix[j])
        arr.append(b)
    k,l = 0,0
    while k<m and l<n:
        for i in range(l,n):
            print(arr[k][i],end=" ")
        k+=1
        for i in range(k,m):
            print(arr[i][n-1],end=" ")
        n-=1
        if k<m:
            for i in range(n-1,l-1,-1):
                print(arr[m-1][i],end=" ")
            m-=1
        if l<n:
            for i in range(m-1,k-1,-1):
                print(arr[i][l],end=" ")
            l+=1
    print()
