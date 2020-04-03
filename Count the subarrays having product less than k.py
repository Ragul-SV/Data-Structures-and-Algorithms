t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    start = 0
    res = 0
    j = 1
    for i in range(n):  # i is the end index of subarrays
        j = j*arr[i]
        while start<i and j>=k:
            j = j/arr[start]
            start+=1
        if j<k:
            res += i-start+1
    print(res)
