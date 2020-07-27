t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    start,end = 0,0
    res = 0
    j = 1
    while end<n:  # end is the end index of subarrays
        j = j*arr[i]
        while start<end and j>=k:
            j = j/arr[start]
            start+=1
        if j<k:
            res += end-start+1
        end+=1
    print(res)
