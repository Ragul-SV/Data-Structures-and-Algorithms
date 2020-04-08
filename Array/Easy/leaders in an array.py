t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    max_from_right = -1
    ans = []
    for i in range(n-1,-1,-1):
        if arr[i]>=max_from_right:
            ans.append(arr[i])
        max_from_right = max(max_from_right,arr[i])
    for i in range(len(ans)-1,-1,-1):
        print(ans[i],end=" ")
    print()
