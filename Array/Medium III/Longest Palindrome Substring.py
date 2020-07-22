def longestPalindrome(arr):
    n = len(s)
    dp = [[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        dp[i][i] = True
    maxlen = 1
    st = 0
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            dp[i][i+1] = True
            if maxlen!=2:
                st = i
            maxlen = 2
    for k in range(3,n+1):
        for i in range(n-k+1):
            j = i+k-1
            if dp[i+1][j-1]==True and arr[i]==arr[j]:
                dp[i][j] = True
                if k>maxlen:
                    if k!=maxlen:
                        st = i
                    maxlen = k
    return arr[st:st+maxlen]
