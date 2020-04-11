t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    flag = 0
    for i in range(n-1):
        if not flag and arr[i]>arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        elif flag and arr[i]<arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]
        flag = not flag
    for i in arr:
        print(i,end=" ")
    print()
