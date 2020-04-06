t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = []
    for i in range(n):
        while len(s)!=0 and arr[i]<=s[-1]:
            s.pop()
        if len(s)==0:
            print(-1,end=" ")
        else:
            print(s[-1],end=" ")
        s.append(arr[i])
    print()
