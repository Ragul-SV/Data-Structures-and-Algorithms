def premedian(arr,l,h):
    if l>h:
        return
    if l==h:
        print(arr[l],end=" ")
        return
    flag=0
    for i in range(l+1,h+1):
        if arr[i]>arr[l]:
            flag=1
            break
    if flag==0:
        premedian(arr,l+1,h)
    else:
        premedian(arr,l+1,i-1)
        premedian(arr,i,h)

t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    premedian(arr,0,n-1)
    print()
