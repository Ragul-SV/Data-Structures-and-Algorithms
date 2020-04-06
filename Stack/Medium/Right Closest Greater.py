t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = []
    res = [0]*(n+1)
    for i in range(n-1,-1,-1):
        while len(s)!=0 and s[-1]<=arr[i]:
            s.pop()
        if len(s)!=0:
            res[i] = s[-1]
        s.append(arr[i])
    MOD = 1000000001
    ans = 0
    for i in res:
        ans = (ans+i)%MOD
    print(ans)
