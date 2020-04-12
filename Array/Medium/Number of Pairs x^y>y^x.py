#--------------------------------METHOD1--------O(N^2)---------------------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    c = 0
    for x in range(m):
        for y in range(n):
            if arr1[x]**arr2[y]>arr2[y]**arr1[x]:
                c+=1
    print(c)
#--------------------------------METHOD2---------O(NLOGN+MLOGM)------------------------------------------------------------------------#
import bisect
def countPairs(x,arr2,n,y):
    if x==0:
        return 0
    if x==1:
        return y[0]
    # index = n
    # for i in range(n):
    #     if arr2[i]>x:
    #         index = i
    #         break
    index = bisect.bisect_right(arr2,x)
    res = n - index
    res += y[0]+y[1]
    if x==2:
        res-=y[3]+y[4]
    if x==3:
        res+=y[2]
    return res

t = int(input())
for cases in range(t):
    m,n = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    arr2.sort()
    y = [0]*5
    for i in range(n):
        if arr2[i]<5:
            y[arr2[i]]+=1
    c = 0
    for x in arr1:
        c+=countPairs(x,arr2,n,y)
    print(c)
