t = int(input())
for cases in range(t):
    n,q = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    unread = dict()
    read = dict()
    trash = dict()
    cu = 0
    cr = 0
    ct = 0
    for i in range(1,n+1):
        unread[i] = cu
        cu+=1
    for i in range(0,2*q,2):
        if arr[i]==1:
            del unread[arr[i+1]]
            read[arr[i+1]] = cr
            cr+=1
        elif arr[i]==2:
            del read[arr[i+1]]
            trash[arr[i+1]] = ct
            ct+=1
        elif arr[i]==3:
            del unread[arr[i+1]]
            trash[arr[i+1]] = ct
            ct+=1
        elif arr[i]==4:
            del trash[arr[i+1]]
            read[arr[i+1]] = cr
            cr+=1
    if len(unread)==0:
        print("EMPTY")
    else:
        for i in unread:
            print(i,end=" ")
        print()
    if len(read)==0:
        print("EMPTY")
    else:
        for key,value in sorted(read.items(),key=lambda x:x[1]):
            print(key,end=" ")
        print()
    if len(trash)==0:
        print("EMPTY")
    else:
        for key,value in sorted(trash.items(),key=lambda x:x[1]):
            print(key,end=" ")
        print()
