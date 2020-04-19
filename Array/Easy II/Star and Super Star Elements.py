t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    L = [0]*n
    R = [0]*n
    L[0] = -2**31
    R[n-1] = -2**31
    for i in range(1,n):
        L[i] = max(arr[i-1],L[i-1])
    for i in range(n-2,-1,-1):
        R[i] = max(arr[i+1],R[i+1])
    res = []
    for i in range(n):
        if arr[i]>L[i] and arr[i]>R[i]:
            res.append(arr[i])
        if arr[i]>R[i]:
            print(arr[i],end=" ")
            flag = 1
    if not flag:
        print(-1)
    else:
        print()
    if res:
        for i in res:
            print(i,end=" ")
        print()
    else:
        print(-1)
