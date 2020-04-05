t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    d = dict()
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]] = [i]
        else:
            d[arr[i]].append(i)
    l = list(d.keys())
    l.sort()
    flag = 0
    max_length = 0
    min_num = 0
    for i in range(len(l)-1):
        if l[i]+1!=l[i+1]:
            max_length = max(max_length,i+1-min_num)
            min_num = i+1
    max_length = max(max_length,len(l)-min_num)
    print(max_length)
