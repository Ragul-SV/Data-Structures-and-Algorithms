def printDuplicates(arr, n):
    flag = 0
    d = dict()
    for i in range(n):
        arr[arr[i]%n]+=n
        
    for i in range(n):
        if arr[i]//n>1:
            print(i,end=" ")
            flag = 1
        
    if not flag:
        print(-1,end=" ")
