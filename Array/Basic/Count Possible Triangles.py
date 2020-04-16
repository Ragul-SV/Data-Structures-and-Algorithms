t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    c = 0
    for end in range(n-1,1,-1):
        l = 0
        r = end-1
        while l<r:
            if arr[l]+arr[r]>arr[end]:
                c+=r-l
                r-=1
            else:
                l+=1
    print(c)
