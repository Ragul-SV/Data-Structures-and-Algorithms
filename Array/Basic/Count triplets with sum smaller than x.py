t = int(input())
for cases in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    if n<3:
        print(0)
    else:
        arr.sort()
        c = 0
        for i in range(n-2):
            j = i+1
            k = n-1
            while j<k:
                if arr[i]+arr[j]+arr[k]<x:
                    c+=k-j
                    j+=1
                else:
                    k-=1
        print(c)
