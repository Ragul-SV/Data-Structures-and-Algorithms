t = int(input())
for cases in range(t):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = []
    st = []
    for i in range(n-1,-1,-1):
        while len(st)!=0 and arr[i]>=st[-1]:
            st.pop()
        if len(st)==0:
            res.append(-1)
        else:
            res.append(st[-1])
        st.append(arr[i])
    for i in range(n-1,-1,-1):
        print(res[i],end=" ")
    print()
