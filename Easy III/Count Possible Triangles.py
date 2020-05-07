#---------------------------METHOD1----------------O(N^3)-------------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    c = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]>arr[k] and arr[i]+arr[k]>arr[j]\
                and arr[j]+arr[k]>arr[i]:
                    c+=1
    print(c)
#-------------------------METHOD2------------------O(N^3) TO O(N^2)--------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    c = 0
    for i in range(n-2):
        k = i+2
        for j in range(i+1,n):
            while k<n and arr[i]+arr[j]>arr[k]:
                k+=1
            if k>j:
                c+=k-j-1
    print(c)
#-----------------------METHOD3--------------------O(N^2)---------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    c = 0
    for i in range(n-1,0,-1):
        l = 0
        r = i-1
        while l<r:
            if arr[l]+arr[r]>arr[i]:
                c+=r-l
                r-=1
            else:
                l+=1
    print(c)
