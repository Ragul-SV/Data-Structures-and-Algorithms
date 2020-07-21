#-------------------------------O(N)------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    flag = 0
    if n==2 and arr[0]>arr[1]:
        print(1)
    elif arr[n-2]>arr[n-1]:
        print(n-1)
    else:
        for i in range(1,n-1):
            if arr[i-1]>arr[i] and arr[i]<=arr[i+1]:
                print(i)
                flag = 1
                break
        if flag==0:
            print(0)

#------------------------------O(LogN)----------------------------------------#
def NumberOfRotations(arr,n):
    l,r = 0,n-1
    while l<=r:
        mid = (l+r)//2
        if l==r:
            return l
        if mid>l and arr[mid]<arr[mid-1]:
            return mid
        if mid<r and arr[mid]>arr[mid+1]:
            return mid+1
        if arr[r]>arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return 0
