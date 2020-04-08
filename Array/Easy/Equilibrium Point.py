t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = sum(arr)
    flag = 0
    sum_l,sum_r = 0,0
    for i in range(n):
        if i+1>=n:
            sum_r = 0
        else:
            sum_r = s-sum_l-arr[i]
        if sum_l==sum_r:
            print(i+1)
            flag = 1
            break
        sum_l += arr[i]
    if flag==0:
        print(-1)
