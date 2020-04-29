t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    i = 0
    s = 0
    while i<n:
        if arr[i]>k:
            i+=1
            continue
        count = 0
        while i<n and arr[i]<=k:
            count+=1
            i+=1
        s += count*(count+1)//2
    print(n*(n+1)//2 - s)
