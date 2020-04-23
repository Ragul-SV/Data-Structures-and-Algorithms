def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    #print the required output
    #no need to print new line
    arr2.sort()
    for i in range(n1):
        l,r = 0,n2-1
        while l<=r:
            mid = (l+r)//2
            if arr2[mid]<=arr1[i]:
                l = mid+1
            else:
                r = mid-1
        print(l,end=" ")
