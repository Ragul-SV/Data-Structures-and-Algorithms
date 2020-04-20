t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    start,end = 0,0
    cursum = 0
    minlen = n+1
    while end<n:
        while cursum<=k and end<n:
            if cursum<=0 and k>0:
                start = end
                cursum = 0
            cursum += arr[end]
            end+=1
        while cursum>k and start<=end:
            if end-start<minlen:
                minlen = end-start
            cursum -= arr[start]
            start+=1
    print(minlen)
