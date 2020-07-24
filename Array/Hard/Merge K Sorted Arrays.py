def merge(arr1,arr2,n1,n2,out):
    i,j,k = 0,0,0
    while i<n1 and j<n2:
        if arr1[i]<arr2[j]:
            out[k] = arr1[i]
            i+=1
        else:
            out[k] = arr2[j]
            j+=1
        k+=1
    while i<n1:
        out[k] = arr1[i]
        i+=1
        k+=1
    while j<n2:
        out[k] = arr2[j]
        j+=1
        k+=1

def mergeK(arr,i,j,k,res):
    if i==j:
        for p in range(k):
            res[p] = arr[i][p]
        return
    if (j-i) == 1:
        merge(arr[i],arr[j],k,k,res)
        return
    out1 = [0]*(k*(((i+j)//2)-i+1))
    out2 = [0]*(k*(j-((i+j)//2)))
    mergeK(arr,i,(i+j)//2,k,out1)
    mergeK(arr,((i+j)//2)+1,j,k,out2)
    merge(out1,out2,(k*(((i+j)//2)-i+1)),(k*(j-((i+j)//2))),res)
    
def mergeKArrays(arr,k):
    res = [0]*(k*k)
    mergeK(arr,0,k-1,k,res)
    return res
