t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    m = int(input())
    if m>=n:
        print(0)
    else:
        d = dict()
        for i in range(n):
            if arr[i] not in d:
                d[arr[i]] = 1
            else:
                d[arr[i]] += 1
        l = sorted(d.values())
        for i in range(len(l)):
            p = l[i]
            for j in range(p):
                m = m-1
                l[i] = l[i]-1
                if m==0:
                    break
            if m==0:
                break
        c = 0
        for i in range(len(l)):
            if l[i]!=0:
                c+=1
        print(c)
        
