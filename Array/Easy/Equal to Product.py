t = int(input())
for cases in range(t):
    n,k = input().split()
    n = int(n)
    k = int(k)
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
    flag = 0
    for i in range(n):
        if arr[i]!=0 and k/arr[i] in d:
            if len(d[k/arr[i]])>1 or d[k/arr[i]][0]!=i:
                flag = 1
                break
    if flag:
        print("Yes")
    else:
        print("No")
