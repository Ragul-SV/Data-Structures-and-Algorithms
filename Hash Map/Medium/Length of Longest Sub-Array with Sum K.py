t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    s = 0
    d = dict()
    max_length = 0
    for i in range(n):
        s += arr[i]
        if s==k:
            max_length = max(max_length,i+1)
        if s-k in d:
            max_length = max(max_length,i-d[s-k])
        if s not in d:
            d[s] = i
    print(max_length)
