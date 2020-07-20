#------------------------------------------------O(4^N)----------------------------------------------------#
def phoneDigits(arr,cur,n,temp,res):
    if cur==n:
        res.append("".join(temp))
        return
    for i in range(len(d[arr[cur]])):
        temp.append(d[arr[cur]][i])
        phoneDigits(arr,cur+1,n,temp,res)
        temp.pop()
        if arr[cur]==0 or arr[cur]==1:
            return 
    
##Complete this function
def possibleWords(arr,n):
    res = []
    temp = []
    phoneDigits(arr,0,n,temp,res)
    return res
