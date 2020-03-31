t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(str,input().strip().split()))
    d = dict()
    q = []
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = 1
            q.append(arr[i])
        else:
            if arr[i] in q:
                q.pop(q.index(arr[i]))
        if q:
            print(q[0],end=" ")
        else:
            print(-1,end=" ")
    print()
