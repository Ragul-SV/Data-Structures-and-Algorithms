def final(arr,n):
    st = []
    for i in range(len(arr)):
        while st and arr[i]<0 and st[-1]>0:
            if -arr[i]>st[-1]:
                st.pop()
                continue
            elif -arr[i]==st[-1]:
                st.pop()
            break
        else:
            st.append(arr[i])
    return st
        
