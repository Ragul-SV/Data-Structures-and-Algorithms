#------------------METHOD1-------USING HASHING--------O(N^2)--------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n,k = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
    flag = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if k-(arr[i]+arr[j]) in d:
                for z in range(len(d[k-(arr[i]+arr[j])])):
                    if d[k-(arr[i]+arr[j])][z]!=i and d[k-(arr[i]+arr[j])][z]!=j:
                        print(1)
                        flag = 1
                        break
            if flag==1:
                break
        if flag==1:
            break
    if flag==0:
        print(0)
#--------------------METHOD2-----------USING TWO POINTER APPROACH---------O(N^2)------------------------------------------------------#
t = int(input())
for cases in range(t):
    n,k = map(int,input().strip().split())
    arr = list(map(int,input().strip().split()))
    arr.sort()
    flag = 0
    for i in range(n-2):
        low = i+1
        high = n-1
        while low<high:
            if arr[i]+arr[low]+arr[high]==k:
                print(1)
                flag = 1
                break
            elif arr[i]+arr[low]+arr[high]>k:
                high-=1
            else:
                low+=1
        if flag==1:
            break
    if flag==0:
        print(0)
