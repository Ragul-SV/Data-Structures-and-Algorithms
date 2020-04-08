t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    l = [0]*n
    r = [0]*n
    l[0] = arr[0]
    for i in range(1,n):
        l[i] = min(arr[i],l[i-1])
    r[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        r[i] = max(arr[i],r[i+1])
    max_length = -1
    print(l,r)
    i,j = 0,0
    while i<n and j<n:
        if l[i]<r[j]:
            max_length = max(max_length,j-i)
            j+=1
        else:
            i+=1
    print(max_length)
