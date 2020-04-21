t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    arr1.sort()
    arr2.sort()
    k = int(input())
    res_l,res_r = 0,0
    l,r = 0,n-1
    diff = 2**31
    while l<m and r>=0:
        if abs(arr1[l]+arr2[r]-k)<diff:
            diff = abs(arr1[l]+arr2[r]-k)
            res_l = l
            res_r = r
        if (arr1[l]+arr2[r])>k:
            r-=1
        else:
            l+=1
    print(arr1[res_l],arr2[res_r])
    
