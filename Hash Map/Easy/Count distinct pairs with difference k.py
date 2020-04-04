t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    d = dict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
    c = 0
    for i in range(n):
        if (k+arr[i]) in d and not (len(d[k+arr[i]])==1 and d[k+arr[i]][0]==i):
            c+=1
            del d[k+arr[i]]
    print(c)
