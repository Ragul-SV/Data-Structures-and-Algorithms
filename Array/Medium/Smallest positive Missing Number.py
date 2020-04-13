t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    j = 0
    for i in range(n):
        if arr[i]<0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    index = -1       
    for i in range(n):
        if arr[i]>0:
            index = i
            break
    if index==-1:
        print(1)
    else:
        for i in range(index,n):
            if abs(arr[i])+index-1<n and arr[abs(arr[i])+index-1]>0:
                arr[abs(arr[i])+index-1]*=-1
        flag = 0
        for i in range(index,n):
            if arr[i]>0:
                res = i-index+1
                flag = 1
                break
        if flag==0:
            res = n-index+1
        print(res)
