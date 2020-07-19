def printmat(m, n, arr):
    s = set()
    for i in range(m):
        st = ""
        for j in range(i*n,i*n+n):
            st+=str(arr[j])
        if st not in s:
            s.add(st)
            for i in range(n):
                print(st[i],end=" ")
            print("$",end="")
    print()
