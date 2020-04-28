def kadane(arr,n):
    max_ending_here = 0
    max_so_far = 0
    for i in range(n):
        max_ending_here += arr[i]
        if max_ending_here<0:
            max_ending_here = 0
        elif max_ending_here>max_so_far:
            max_so_far = max_ending_here
    return max_so_far
    
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    flag = 1
    for i in range(n):
        if arr[i]>0:
            flag = 0
            break
    if flag:
        print(max(arr))
    else:
        max_kadane = kadane(arr,n)
        max_wrap = 0
        for i in range(n):
            max_wrap += arr[i]
            arr[i] = -arr[i]
        max_wrap = max_wrap + kadane(arr,n)
        print(max(max_kadane,max_wrap))
