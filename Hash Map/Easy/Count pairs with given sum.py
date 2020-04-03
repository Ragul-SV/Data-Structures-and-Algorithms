t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if k-arr[i]>=0:
            if k-arr[i] in d:
                d[k-arr[i]].append(i)
            else:
                d[k-arr[i]] = [i]
    c = 0
    for i in range(n):
        if arr[i] in d:
            for j in range(len(d[arr[i]])):
                if d[arr[i]][j]>i:
                    c+=1
    print(c)
