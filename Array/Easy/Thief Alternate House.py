#--------METHOD1----TIME COMPLEXITY:O(N)----SPACE COMPLEXITY:O(N)------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    if n==0:
        print(0)
    elif n==1:
        print(arr[0])
    elif n==2:
        print(max(arr[0],arr[1]))
    else:
        dp = [0]*n
        dp[0] = arr[0]
        dp[1] = max(arr[0],arr[1])
        for i in range(2,n):
            dp[i] = max(arr[i]+dp[i-2],dp[i-1])
        print(dp[-1])
#--------METHOD2----TIME COMPLEXITY:O(N)----SPACE COMPLEXITY:O(1)------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    if n==0:
        print(0)
    elif n==1:
        print(arr[0])
    elif n==2:
        print(max(arr[0],arr[1]))
    else:
        val1 = arr[0]
        val2 = max(arr[0],arr[1])
        max_val = 0
        for i in range(2,n):
            max_val = max(arr[i]+val1,val2)
            val1 = val2
            val2 = max_val
        print(max_val)
