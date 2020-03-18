def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
 
def isBST(root):
    arr = []
    inorder(root,arr)
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True
