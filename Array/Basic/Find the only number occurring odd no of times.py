t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = 0
    for i in range(n):
        res = res^arr[i]
    print(res)
