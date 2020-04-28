t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = 0
    i = 0
    oneFound = False
    while i<n:
        if arr[i]==1:
            oneFound = True
        while i<n and arr[i]==1:
            i+=1
        count = 0
        while i<n and arr[i]==0:
            count+=1
            i+=1
        if not oneFound and i==n:
            res = -1
            break
        curr_count = 0
        if i<n and oneFound:
            if count%2==0:
                curr_count = count//2
            else:
                curr_count = (count+1)//2
            count = 0
        else:
            curr_count = count
            count = 0
        res = max(res,curr_count)
    print(res)
