t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    start = 0
    s = 0
    flag = 0
    for i in range(n):
        s+=arr[i]
        while start<i and s>k:
            s-=arr[start]
            start+=1
        if s==k:
            print(start+1,i+1)
            flag = 1
            break

    if flag==0:
        print(-1)
