t = int(input())
for cases in range(t):
    n = int(input())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    d = dict()
    for i in range(len(arr1)):
        if arr1[i] in d:
            d[arr1[i]] += 1
        else:
            d[arr1[i]] = 1
    flag = 1
    for i in range(len(arr2)):
        if arr2[i] not in d:
            flag = 0
            break
        if d[arr2[i]]==0:
            flag = 0
            break
        else:
            d[arr2[i]]-=1
    if flag==1:
        for i in d.keys():
            if d[i]!=0:
                flag = 0
                break
    if flag==0:
        print(0)
    else:
        print(1)
