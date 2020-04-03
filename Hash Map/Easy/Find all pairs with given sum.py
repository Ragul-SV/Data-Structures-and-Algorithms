t = int(input())
for cases in range(t):
    n,m,x = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    arr1.sort()
    d = dict()
    for i in range(m):
        d[(x-arr2[i])] = 1
    s = ""
    flag = 0
    for i in range(n):
        if arr1[i] in d:
            s += str(arr1[i])+" "+str(x-arr1[i])+","+" "
            flag = 1
    if flag == 1:
        print(s[:-2])
    else:
        print(-1)
