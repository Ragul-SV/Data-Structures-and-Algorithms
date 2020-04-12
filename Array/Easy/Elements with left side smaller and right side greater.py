t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    leftMax = [0]*n
    rightMin = [0]*n
    leftMax[0] = -2**31
    rightMin[n-1] = 2**31
    for i in range(1,n):
        leftMax[i] = max(arr[i-1],leftMax[i-1])
    for i in range(n-2,-1,-1):
        rightMin[i] = min(arr[i+1],rightMin[i+1])
    
    flag = 0
    for i in range(1,n-1):
        if arr[i]>=leftMax[i] and arr[i]<=rightMin[i]:
            print(arr[i])
            flag = 1
            break
    if flag==0:
        print(-1)
