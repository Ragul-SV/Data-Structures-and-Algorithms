t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(str,input().strip().split()))
    arr.sort(key=lambda x:str(x)*10,reverse=True)
    s = ""
    for i in range(n):
        s+=str(arr[i])
    print(s)
