def slidingWindow(arr,n,k):
    q = []
    for i in range(k):
        while q and int(arr[i])>=int(arr[q[-1]]):
            q.pop()
        q.append(i)
    for i in range(k,n):
        print(int(arr[q[0]]),end=" ");
        while q and q[0]<=i-k:
            q.pop(0)
        while q and int(arr[i])>=int(arr[q[-1]]):
            q.pop()
        q.append(i)
    print(int(arr[q[0]]),end=" ")

t = int(input())
for cases in range(t):
    n,k = map(int,input().strip().split())
    arr = input().split()
    slidingWindow(arr,n,k)
    print()
