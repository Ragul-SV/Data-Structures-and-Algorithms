t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    d = dict()
    flag = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]+arr[j] not in d:
                d[arr[i]+arr[j]] = 1
            else:
                print(1)
                flag = 1
                break
        if flag==1:
            break
    if flag==0:
        print(0)
