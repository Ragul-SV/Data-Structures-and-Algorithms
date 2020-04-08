t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    flag = 0
    for i in range(n):
        if arr[i]>0:
            flag = 1
            break
    if flag == 1:
        max_so_far = -2**31
        max_ending_here = 0
        s = 0
        for i in range(0,n):
            max_ending_here+=arr[i]
            max_ending_here = max(0,max_ending_here)
            max_so_far = max(max_so_far,max_ending_here)
        print(max_so_far)
    if flag == 0:
        max_so_far = arr[0]
        curr_max = arr[0]
        s = 0
        for i in range(1,n):
            curr_max = max(curr_max,curr_max+arr[i])
            max_so_far = max(max_so_far,curr_max)
        print(max_so_far)
