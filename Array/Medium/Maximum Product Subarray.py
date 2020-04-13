t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    if n==0:
        print(arr[0])
        continue
    maxval = 1
    minval = 1
    res = 1
    flag = 0
    flag1 = 0
    for i in range(n):
        if arr[i]>0:
            maxval = maxval*arr[i]
            minval = min(minval*arr[i],1)
            flag = 1
        elif arr[i]==0:
            minval = 1
            maxval = 1
            flag1 = 1
        elif arr[i]<0:
            temp = maxval
            maxval = max(minval*arr[i],1)
            minval = temp*arr[i]
        res = max(res,maxval)
    if (not flag and res==1 and flag1):
        print(0)
    else:
        print(res)
        
