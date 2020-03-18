def inorder1(root,arr):
    if root:
        inorder1(root.left,arr)
        arr[root.data]=1
        inorder1(root.right,arr)
 
def inorder2(root,arr):
    if root:
        inorder2(root.left,arr)
        if arr[root.data]==1:
            print(root.data,end=" ")
        inorder2(root.right,arr)
 
def printCommon(root1, root2):
    arr = [0]*10000
    inorder1(root1,arr)
    inorder2(root2,arr)
