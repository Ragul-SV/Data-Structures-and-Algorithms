t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    zero_count = 0
    max_diff = 0
    curr_sum = 0
    for i in range(n):
        if arr[i]==0:
            zero_count+=1
        if arr[i]==0:
            arr[i] = -1
        curr_sum = max(arr[i],curr_sum+arr[i])
        max_diff = max(max_diff,curr_sum)
    max_diff = max(0,max_diff)
    print(zero_count+max_diff)
