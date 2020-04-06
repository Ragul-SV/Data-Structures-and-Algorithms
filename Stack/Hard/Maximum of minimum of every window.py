#-----------------------------------------------------O(n^3)-------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    for k in range(1,n+1):
        max_window = 0
        for i in range(n-k+1):
            min_window = arr[i]
            for j in range(k):
                min_window = min(min_window,arr[i+j])
            max_window = max(max_window,min_window)
        print(max_window,end=" ")
    print()
#----------------------------------------------------O(n)-----------------------------------------------------------------------#
t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = []
    left = [-1]*(n+1)
    right = [n]*(n+1)
    for i in range(n):
        while(len(s)!=0 and arr[s[-1]]>=arr[i]):
            s.pop()
        if len(s)!=0:
            left[i] = s[-1]
        s.append(i)
    s = []
    for i in range(n-1,-1,-1):
        while(len(s)!=0 and arr[s[-1]]>=arr[i]):
            s.pop()
        if len(s)!=0:
            right[i] = s[-1]
        s.append(i) 
    ans = [0]*(n+1)
    for i in range(n):
        length = right[i]-left[i]-1
        ans[length] = max(ans[length],arr[i])
    for i in range(n-1,0,-1):
        ans[i] = max(ans[i],ans[i+1])
    for i in range(1,n+1):
        print(ans[i],end=" ")
    print()
