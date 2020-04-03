def countDistinct(arr, n, k):
    d = dict()
    c = 0
    for i in range(k):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
            c += 1
    print(c,end=" ")
    for i in range(1,n-k+1):
        d[arr[i-1]]-=1
        if d[arr[i-1]]==0:
            c-=1
            del d[arr[i-1]]
        if arr[i+k-1] in d:
            d[arr[i+k-1]] += 1
        else:
            d[arr[i+k-1]] = 1
            c+=1
        print(c,end=" ")
    print()
