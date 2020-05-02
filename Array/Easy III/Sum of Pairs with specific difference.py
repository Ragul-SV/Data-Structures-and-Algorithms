t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    arr.sort()
    dp = [0]*n
    dp[0] = 0
    for i in range(1,n):
        dp[i] = dp[i-1]
        if arr[i]-arr[i-1] < k:
            if i>=2:
                dp[i] = max(dp[i-1],dp[i-2]+arr[i]+arr[i-1])
            else:
                dp[i] = max(dp[i-1],arr[i]+arr[i-1])
    print(dp[n-1])
