t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    dep = list(map(int,input().strip().split()))
    arr.sort()
    dep.sort()
    i,j=1,0
    c = 1
    res = 1
    while i<n and j<n:
        if arr[i]<=dep[j]:
            c+=1
            res = max(res,c)
            i+=1
        else:
            c-=1
            j+=1
    print(res)
