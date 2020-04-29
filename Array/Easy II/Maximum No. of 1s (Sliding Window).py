t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    wL,wR = 0,0
    res = 0
    zero_count = 0
    while wR<n:
        if zero_count<=m:
            if arr[wR]==0:
                zero_count+=1
            wR+=1
        if zero_count>m:
            if arr[wL]==0:
                zero_count-=1
            wL+=1
        if wR-wL>res and zero_count<=m:
            res = wR-wL
    print(res)
        
