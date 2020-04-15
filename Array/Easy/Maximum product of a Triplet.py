#-------------METHOD1---------O(N^LOGN)--------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    print(max(arr[0]*arr[1]*arr[n-1],arr[n-3]*arr[n-2]*arr[n-1]))
#-------------METHOD2----------O(N)------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    maxA,maxB,maxC = -2**31,-2**31,-2**31
    minA,minB = 2**31,2**31
    for i in range(n):
        if arr[i]>maxA:
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
        elif arr[i]>maxB:
            maxC = maxB
            maxB = arr[i]
        elif arr[i]>maxC:
            maxC = arr[i]
        
        if arr[i]<minA:
            minB = minA
            minA = arr[i]
        elif arr[i]<minB:
            minB = arr[i]
    print(max(minA*minB*maxA,maxA*maxB*maxC))
