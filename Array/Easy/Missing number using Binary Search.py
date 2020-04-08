def binary_search(arr,l,h):
    if l>h:
        return -1
    mid = (l+h)//2
    if arr[mid]!=mid+1:
        print(mid+1)
    else:
        binary_search(arr,0,mid-1)
        binary_search(arr,mid+1,h)

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    binary_search(arr,0,n-1)
