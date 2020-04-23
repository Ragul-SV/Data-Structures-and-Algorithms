#---------------------------------------METHOD1------------------------------------------#
 path_count(n,m):
    if n==0 or m==0:
        return 1
    return path_count(n-1,m)+path_count(n,m-1)

t = int(input())
for cases in range(t):
    n,m = map(int,input().split())
    print(path_count(n,m))
#--------------------------------------METHOD2-------------------------------------------#
t = int(input())
for cases in range(t):
    n,m = map(int,input().split())
    dp = [[0]*(n+1)]*(m+1) 
    for i in range(n+1):
        dp[0][i] = 1
    for i in range(m+1):
        dp[i][0] = 1
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[m][n])
