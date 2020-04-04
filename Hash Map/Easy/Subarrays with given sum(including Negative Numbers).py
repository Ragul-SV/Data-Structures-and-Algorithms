t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    d = dict()
    c = 0
    s = 0
    for i in range(n):
        s += arr[i]
        if s==k:
            c+=1
        if s-k in d:
            c+=d[s-k]
        if s not in d:
            d[s] = 1
        else:
            d[s] += 1
    print(c)
