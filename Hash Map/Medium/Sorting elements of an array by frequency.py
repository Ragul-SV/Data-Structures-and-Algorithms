t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
        else:
            d[arr[i]] += 1
    for key,value in sorted(sorted(d.items()),key = lambda x:x[1],reverse=True):
        for i in range(value):
            print(key,end=" ")
    print()
