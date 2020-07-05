def find3number(arr, n):
    # code here
    l = [0]*n
    r = [0]*n
    l[0] = -1
    for i in range(1,n):
        if l[i-1]!=-1 and arr[i]>arr[l[i-1]]:
            l[i] = l[i-1]
        elif arr[i]>arr[i-1]:
            l[i] = i-1
        else:
            l[i] = -1
    r[n-1] = -1
    for i in range(n-2,-1,-1):
        if r[i+1]!=-1 and arr[i]<arr[r[i+1]]:
            r[i] = r[i+1]
        elif arr[i]<arr[i+1]:
            r[i] = i+1
        else:
            r[i] = -1
    
    for i in range(n):
        if l[i]!=-1 and r[i]!=-1:
            return [arr[l[i]],arr[i],arr[r[i]]]
    return []
