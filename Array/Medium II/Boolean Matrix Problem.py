t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    mat = []
    for i in range(m):
        mat.append(list(map(int,input().strip().split())))
    row_flag = False
    col_flag = False
    for i in range(m):
        for j in range(n):
            if i==0 and mat[i][j]==1:
                row_flag = True
            if j==0 and mat[i][j]==1:
                col_flag = True
            if mat[i][j]==1:
                mat[i][0] = 1
                mat[0][j] = 1
    for i in range(1,m):
        for j in range(1,n):
            if mat[i][0]==1 or mat[0][j]==1:
                mat[i][j] = 1
    if row_flag:
        for j in range(n):
            mat[0][j] = 1
    if col_flag:
        for i in range(m):
            mat[i][0] = 1
    for i in range(m):
        for j in range(n):
            print(mat[i][j],end=" ")
        print()
