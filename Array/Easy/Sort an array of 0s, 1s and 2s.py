#--------------------------------------------METHOD1-------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ans = [1]*(n)
    zero = 0
    two = n-1
    for i in range(n):
        if arr[i]==0:
            ans[zero] = 0
            zero+=1
        elif arr[i]==2:
            ans[two] = 2
            two-=1
    for i in ans:
        print(i,end=" ")
    print()
 #-------------------------------------------METHOD2------------------------------------------------#
 t = int(input())
 for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    zero = 0
    mid = 0
    two = n-1
    while mid<=two:
        if arr[mid]==0:
            arr[zero],arr[mid] = arr[mid],arr[zero]
            zero+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[two] = arr[two],arr[mid]
            two-=1
    for i in arr:
        print(i,end=" ")
    print()
