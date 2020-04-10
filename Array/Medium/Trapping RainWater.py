#------------------------------METHOD1---------TIME COMPLEXITY:O(N)--------SPACE COMPLEXITY:O(N)----------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    l = [0]*n
    r = [0]*n
    l[0] = arr[0]
    for i in range(1,n):
        l[i] = max(l[i-1],arr[i])
    r[n-1] = arr[n-1]
    for i in range(n-2,-1,-1):
        r[i] = max(r[i+1],arr[i])
    ans = 0
    for i in range(n):
        ans += min(l[i],r[i])-arr[i]
    print(ans)
#------------------------------METHOD2---------TIME COMPLEXITY:O(N)--------SPACE COMPLEXITY:O(1)----------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    l = 0
    r = n-1
    lmax,rmax = 0,0
    res = 0
    while l<r:
        if arr[l]<arr[r]:
            if arr[l]>=lmax:
                lmax = arr[l]
            else:
                res+=lmax-arr[l]
            l+=1
        else:
            if arr[r]>=rmax:
                rmax = arr[r]
            else:
                res+=rmax-arr[r]
            r-=1
    print(res)
