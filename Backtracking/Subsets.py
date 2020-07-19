#----------------------------METHOD1 (Backtracking)------------------------------#
def subsets(arr,n,i,subset,res):
    temp = "".join(list(map(str,subset)))
    if temp not in res:
        res.add(temp)
    for j in range(i,n):
        subset.append(arr[j])
        subsets(arr,n,j+1,subset,res)
        subset.pop(-1)
    return 

1 2 3 3
()(1)(1 2)(1 2 3)(1 2 3 3)(1 3)(1 3 3)(2)(2 3)(2 3 3)(3)(3 3)

def AllSubsets(arr,n):
    res = set()
    subset = []
    subsets(arr,n,0,subset,res)
    return sorted(res)
#----------------------------METHOD2 (Power Set)------------------------------#
def AllSubsets(arr,n):
    s = set()
    for i in range(2**n):
        subset = ""
        for j in range(n):
            if (i & 1<<j)!=0:
                subset+=str(arr[j])+'*'
        subset = subset[:-1]
        if subset not in s:
            s.add(subset)
    res = []
    for i in s:
        res.append(i.split('*'))
    return sorted(res)
