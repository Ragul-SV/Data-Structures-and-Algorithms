t = int(input())
for cases in range(t):
    n = int(input())
    arr = [0]*(n+1)
    q = [x for x in range(1,n+1)]
    k = 1
    for i in range(1,n+1):
        for j in range(k):
            q.append(q.pop(0))
        arr[q[0]] = i
        q.pop(0)
        k+=1
    for i in range(1,n+1):
        print(arr[i],end=" ")
    print()
