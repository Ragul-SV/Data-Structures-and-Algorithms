t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    d = dict()
    for i in range(m):
        d[arr1[i]] = 1
    for i in range(n):
        if arr2[i] in d:
            d[arr2[i]] = 0
    c = 0
    for i in d.keys():
        if d[i]==0:
            c+=1
    print(c)
