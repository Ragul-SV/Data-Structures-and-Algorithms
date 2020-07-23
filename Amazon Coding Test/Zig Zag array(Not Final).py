def minOperations(arr):
    n = len(arr)
    c1,c2 = 0,0
    for i in range(1,n,2):
        if i==n-1:
            if arr[i-1]<=arr[i]:
                c1 += arr[i]-arr[i-1]+1
        else:
            if arr[i-1]<=arr[i] or arr[i+1]<=arr[i]:
                c1+= arr[i]-min(arr[i-1],arr[i+1])+1
    for i in range(n,2):
        if i==0:
            if arr[i+1]<=arr[i]:
                c2 += arr[i]-arr[i+1]+1
        elif i==n-1:
            if arr[i-1]<=arr[i]:
                c2 += arr[i]-arr[i-1]+1
        else:
            if arr[i-1]<=arr[i] or arr[i+1]<=arr[i]:
                c2+= arr[i]-min(arr[i-1],arr[i+1])+1
    return min(c1,c2)
