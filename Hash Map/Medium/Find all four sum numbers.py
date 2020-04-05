t = int(input())
for cases in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().strip().split()))
    d = dict()
    if n<4:
        print(-1)
    else:
        flag = 0
        for i in range(n-1):
            for j in range(i+1,n):
                s = arr[i] + arr[j]
                if s not in d:
                    d[s] = [[i,j]]
                else:
                    d[s].append([i,j])
        d1 = dict()            
        for i in range(n-1):
            for j in range(i+1,n):
                s = arr[i] + arr[j]
                if k-s in d:
                    for z in range(len(d[k-s])):
                        if d[k-s][z][0]!=i and d[k-s][z][0]!=j and d[k-s][z][1]!=i and d[k-s][z][1]!=j:
                            l=[arr[d[k-s][z][0]],arr[d[k-s][z][1]],arr[i],arr[j]]
                            l.sort()
                            st = ""
                            for y in l:
                                st+=str(y)+" "
                            if st not in d1:
                                d1[st] = 1
                                flag = 1
        if flag==0:
            print(-1)
        else:
            l = []
            for i in d1:
	            l.append(list(map(int,i.split())))
            l.sort()
            for i in l:
                for j in range(len(i)):
                    print(i[j],end=" ")
                print("$",end="")
            print()
