t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    i = 0
    while i<n:
        l = i
        r = min(i+k-1,n-1)
        while l<r:
            arr[l],arr[r] = arr[r],arr[l]
            l+=1
            r-=1
        i+=k
    for i in arr:
        print(i,end=" ")
    print()
