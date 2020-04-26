t = int(input())
for cases in range(t):
    n,m = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    c = 0
    i,j = n-1,m-1
    res = []
    while i>=0 and j>=0:
        s = arr1[i]+arr2[j]
        if c==1:
            s+=1
        if s//10==1:
            s = s%10
            c = 1
        else:
            c = 0
        res.append(s)
        i-=1
        j-=1
    while i>=0:
        s = arr1[i]
        if c==1:
            s+=1
        if s//10==1:
            s = s%10
            c = 1
        else:
            c = 0
        res.append(s)
        i-=1
    while j>=0:
        s = arr2[j]
        if c==1:
            s+=1
        if s//10==1:
            s = s%10
            c = 1
        else:
            c = 0
        res.append(s)
        j-=1
    if c==1:
        res.append(c)
    for i in range(len(res)-1,-1,-1):
        print(res[i],end=" ")
    print()
        
