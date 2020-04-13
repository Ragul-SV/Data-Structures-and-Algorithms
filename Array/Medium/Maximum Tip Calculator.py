t = int(input())
for cases in range(t):
    n,x,y = map(int,input().split())
    arr1 = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    arr = []
    for i in range(n):
        arr.append([arr1[i],arr2[i]])
    arr.sort(key=lambda x:abs(x[1]-x[0]),reverse=True)
    c = 0
    for i in range(n):
        if x>0 and (arr[i][0]>=arr[i][1] or y==0):
            c+=arr[i][0]
            x-=1
        elif y>0 and (arr[i][1]>arr[i][0] or x==0):
            c+=arr[i][1]
            y-=1
    print(c)
