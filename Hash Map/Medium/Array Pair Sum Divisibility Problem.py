t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    k = int(input())
    d = dict()
    if n%2!=0:
        print(False)
    else:
        if k==1:
            print(True)
        else:
            for i in range(n):
                if arr[i]%k not in d:
                    d[arr[i]%k] = 1
                else:
                    d[arr[i]%k]+=1
            flag = True
            for i in range(n):
                if arr[i]%k==k/2:
                    if d[arr[i]%k]%2!=0:
                        flag = False
                        break
                elif arr[i]%k==0:
                    if d[arr[i]%k]%2!=0:
                        flag = False
                        break
                elif k-(arr[i]%k) in d:
                    if d[arr[i]%k]!=d[k-(arr[i]%k)]:
                        flag = False
                        break
                else:
                    flag = False
                    break
            print(flag)
            
