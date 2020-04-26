def binary_search(arr,k,flag):
    l,r = 0,n-1
    while l<=r:
        mid = (l+r)//2
        if (arr[mid]==k and flag) or arr[mid]>k:
            r = mid-1
        else:
            l = mid+1
    if flag:
        return l
    else:
        return r

t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    start = binary_search(arr,k,1)
    if start==n or arr[start]!=k:
        print(-1)
    else:
        print(start,binary_search(arr,k,0))
