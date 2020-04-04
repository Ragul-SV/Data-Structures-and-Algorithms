t = int(input())
d = dict()
l = [0,1]
d[0] = 1
d[1] = 1
i = 2
f = 1
while l[-2]+l[-1]<=1000:
    d[l[-2]+l[-1]] = 1
    l.append(l[-2]+l[-1])
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = []
    for i in range(n):
        if arr[i] in d:
            print(arr[i],end=" ")
    print()
