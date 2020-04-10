#-------------------METHOD1--------O((N+M)LOG(N+M))-----------------------------------------------------------------------------------#
def nextGap(gap):
    if gap<=1:
        return 0
    return gap//2 + gap%2

t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    gap = nextGap(m+n)
    while gap>0:
        i = 0
        while i+gap<m:
            if arr1[i]>arr1[i+gap]:
                arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]
            i+=1
        if gap>m:
            j = gap-m
        else:
            j = 0
        while i<m and j<n:
            if arr1[i]>arr2[j]:
                arr1[i],arr2[j] = arr2[j],arr1[i]
            i+=1
            j+=1
        if j<n:
            j = 0
            while j+gap<n:
                if arr2[j]>arr2[j+gap]:
                    arr2[j],arr2[j+gap] = arr2[j+gap],arr2[j]
                j+=1
        gap = nextGap(gap)
    for i in range(m):
        print(arr1[i],end=" ")
    print()
    for i in range(n):
        print(arr2[i],end=" ")
    print()
#----------------------METHOD2--------------O(NLOGN+MLOGM)----------------------------------------------------------------------#
def nextGap(gap):
    if gap<=1:
        return 0
    return gap//2 + gap%2

t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    x = min(m,n)
    for i in range(x):
        if arr1[m-i-1]>arr2[i]:
            arr1[m-i-1],arr2[i] = arr2[i],arr1[m-i-1]
    gap = nextGap(m)
    while gap>0:
        i = 0
        while i+gap<m:
            if arr1[i]>arr1[i+gap]:
                arr1[i],arr1[i+gap] = arr1[i+gap],arr1[i]
            i+=1
        gap = nextGap(gap)
    
    gap = nextGap(n)
    while gap>0:
        i = 0
        while i+gap<n:
            if arr2[i]>arr2[i+gap]:
                arr2[i],arr2[i+gap] = arr2[i+gap],arr2[i]
            i+=1
        gap = nextGap(gap)
        
    for i in range(m):
        print(arr1[i],end=" ")
    print()
    for i in range(n):
        print(arr2[i],end=" ")
    print()
#---------------------------METHOD3-------O(N*M)----------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    for i in range(n-1,-1,-1):
        last = arr1[m-1]
        j = m-2
        while j>=0 and arr1[j]>arr2[i]:
            arr1[j+1] = arr1[j]
            j-=1
        if j!=m-2 or last>arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last
        print(arr1,arr2,i,j)
    for i in arr1:
        print(i,end=" ")
    print()
    for i in arr2:
        print(i,end=" ")
    print()
#-------------------------METHOD4-------O(N+M)------------------------------------------------------------------------------#
def nextGap(gap):
    if gap<=1:
        return 0
    return gap//2 + gap%2

t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    i,j,k = 0,0,0
    while k<m and i<m and j<n:
        if arr1[i]<arr2[j]:
            print(arr1[i],end=" ")
            i+=1
        else:
            print(arr2[j],end=" ")
            j+=1
        k+=1
    while k<m and i<m:
        print(arr1[i],end=" ")
        i+=1
        k+=1
    while k<m and j<n:
        print(arr2[j],end=" ")
        j+=1
        k+=1
    k = 0
    while k<n and i<m and j<n:
        if arr1[i]<arr2[j]:
            print(arr1[i],end=" ")
            i+=1
            k+=1
        else:
            print(arr2[j],end=" ")
            j+=1
            k+=1
    while k<n and i<m:
        print(arr1[i],end=" ")
        i+=1
        k+=1
    while k<n and j<n:
        print(arr2[j],end=" ")
        j+=1
        k+=1
    print()
