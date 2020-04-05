t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    d = dict()
    s = 0
    max_length = 0
    for i in range(n):
        s+=arr[i]
        if s%k==0:
            max_length = max(max_length,i+1)
        if s%k not in d:
            d[s%k] = i
        else:
            max_length = max(max_length,i-d[s%k])
    print(max_length)
