t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    inc = arr[0]
    exc = 0
    for i in range(1,n):
        temp = max(inc,exc)
        inc = exc + arr[i]
        exc = temp
    print(max(inc,exc))
