t = int(input())
for cases in range(t):
    n,m = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr1[i] not in d:
            d[arr1[i]] = 1
        else:
            d[arr1[i]] += 1
    l = []
    for i in range(m):
        if arr2[i] in d:
            for j in range(d[arr2[i]]):
                print(arr2[i],end=" ")
            del d[arr2[i]]
    for i in sorted(d.keys()):
        for j in range(d[i]):
            print(i,end=" ")
    print()
