t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    max_sum = 0
    res = []
    l = []
    s = 0
    flag = 1
    for i in range(n):
        if arr[i]>=0:
            l.append(arr[i])
            s+=arr[i]
        else:
            if l:
                flag = 0
                if s>max_sum:
                    res = l[:]
                    max_sum = s
                elif s==max_sum:
                    if len(l)>len(res):
                        res = l[:]
            l = []
            s = 0
    if s>max_sum:
        res = l[:]
    elif s==max_sum:
        if len(l)>len(res):
            res = l[:]
    if flag==1:
        res = l[:]
    for i in res:
        print(i,end=" ")
    print()
