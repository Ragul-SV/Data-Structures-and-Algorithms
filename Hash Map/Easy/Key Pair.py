t = int(input())
for cases in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if x-arr[i]>0:
            if (x-arr[i]) in d:
                d[(x-arr[i])].append(i)
            else:
                d[(x-arr[i])] = [i]
    flag = 0
    for i in range(n):
        if arr[i] in d:
            if len(d[arr[i]])>1:
                print("Yes")
                flag = 1
                break
            elif d[arr[i]][0]!=i:
                print("Yes")
                flag = 1
                break
    if flag==0:
        print("No")
