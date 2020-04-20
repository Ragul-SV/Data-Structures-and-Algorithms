t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    i = 0
    k = 0
    while k<n and arr[i]==0:
        arr.append(arr.pop(0))
        k+=1
        
    while k<n:
        if arr[i+1]==0:
            arr.append(arr.pop(i+1))
        elif arr[i]==arr[i+1]:
            arr[i]*=2
            arr.pop(i+1)
            arr.append(0)
        else:
            i+=1
        k+=1
        
    for i in arr:
        print(i,end=" ")
    print()
