t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    k = int(input())
    c = 0
    d = dict()
    for i in range(n):
        d[arr2[i]] = 1
    for i in range(m):
        if k-arr1[i] in d:
            c+=1
    print(c)
