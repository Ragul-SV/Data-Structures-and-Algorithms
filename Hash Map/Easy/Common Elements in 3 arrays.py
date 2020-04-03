t = int(input())
for cases in range(t):
    n1,n2,n3 = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    arr3 = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n1):
        d[arr1[i]] = 1
    for i in range(n2):
        if arr2[i] in d and d[arr2[i]]==1:
            d[arr2[i]] += 1
    for i in range(n3):
        if arr3[i] in d and d[arr3[i]]==2:
            d[arr3[i]] += 1
    flag = 0
    for i in sorted(d):
        if d[i]==3:
            print(i,end=" ")
            flag = 1
    if flag == 0:
        print(-1)
    else:
        print()
    
