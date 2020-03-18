def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
 
def isTriplePresent(root):
    arr = []
    inorder(root,arr)
    n = len(arr)
    for i in range(n-2):
        j = i+1
        k = n-1
        while j<k:
            sum = arr[i]+arr[j]+arr[k]
            if sum==0:
                return 1
            elif sum>0:
                k-=1
            else:
                j+=1
    return 0
 
#in-built method    
 
from itertools import combinations
 
def isTriplePresent(root):
    arr = []
    inorder(root,arr)
    c = combinations(arr,3)
    for i in c:
        if sum(i)==0:
            return 1
    return 0
