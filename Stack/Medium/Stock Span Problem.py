t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    s = []
    for i in range(n):
        c = 1
        temp = []
        while len(s)!=0 and s[-1]<=arr[i]:
            c+=1
            temp.append(s.pop())
        print(c,end=" ")
        while temp:
            s.append(temp.pop())
        s.append(arr[i])
    print()
