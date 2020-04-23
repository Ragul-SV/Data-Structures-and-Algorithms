t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    temp = arr[:]
    temp.sort()
    d = dict()
    for i in range(n):
        d[temp[i]] = i
    for i in range(n):
        print(d[arr[i]],end=" ")
    print()
