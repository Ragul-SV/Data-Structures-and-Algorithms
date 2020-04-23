t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    dp = [0]*(n+1)
    dp[0] = 0
    for i in range(1,n+1):
        max_val = -2**31
        for j in range(i):
            max_val = max(max_val,arr[j]+dp[i-j-1])
        dp[i] = max_val
    print(dp[n])
