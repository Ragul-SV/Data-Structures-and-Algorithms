t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    start,end = 0,0
    res = []
    for i in range(n-1):
        if arr[i]<arr[i+1]:
            end+=1
        else:
            if start!=end:
                res.append([start,end])
            start,end = i+1,i+1
    if start!=end:
        res.append([start,end])
    if not res:
        print("No Profit")
    else:
        for i in res:
            print('('+str(i[0])+" "+str(i[1])+')',end=" ")
        print()
    
