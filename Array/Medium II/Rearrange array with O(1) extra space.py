t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    for i in range(n):
        arr.append(int(s[i]))    
    for i in range(n):
        arr[i] += (arr[arr[i]]%n) * n
    for i in range(n):
        print(arr[i]//n,end=" ")
    print()
