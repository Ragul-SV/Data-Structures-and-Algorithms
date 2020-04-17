def findType(arr,n):
    i = 0
    while i<n-1 and arr[i]<arr[i+1]:
        i+=1
    if i==n-1:
        print(arr[n-1],1)
        return 
    if i==0:
        while i<n-1 and arr[i]>arr[i+1]:
            i+=1
        if i==n-1:
            print(arr[0],2)
            return
        if arr[0]>arr[i+1]:
            print(arr[0],4)
            return 
        else:
            print(arr[i+1],3)
            return 
    if i<n-1 and arr[0]>arr[i+1]:
        print(max(arr[0],arr[i]),4)
        return
    else:
        print(max(arr[0],arr[i]),3)
        return     

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    findType(arr,n)
    
