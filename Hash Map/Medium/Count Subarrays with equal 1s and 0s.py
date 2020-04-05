def countSubArray(arr):
    d = dict()
    s = 0
    d[0] = 1
    c = 0
    for i in range(len(arr)):
        if arr[i]==0:
            s-=1
        elif arr[i]==1:
            s+=1
        if s not in d:
            d[s] = 1
        else:
            c+=d[s]
            d[s]+=1
    return c
    
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    print(countSubArray(arr))
