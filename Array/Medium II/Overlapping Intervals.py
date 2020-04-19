t = int(input())
for cases in range(t):
    n = int(input())
    s = list(map(int,input().strip().split()))
    arr = []
    for i in range(0,2*n,2):
        arr.append([s[i],s[i+1]])
    arr.sort(key=lambda x:x[0])
    res = [arr[0]]
    for i in range(1,n):
        if arr[i][0]<=res[-1][1]:
            res[-1][1] = max(res[-1][1],arr[i][1])
        else:
            res.append(arr[i])

    for i in range(len(res)):
        print(res[i][0],res[i][1],end=" ")
    print()
