def preorder(root,arr):
    if root:
        arr.append(root.data)
        preorder(root.left,arr)
        preorder(root.right,arr)
 
def buildBST(arr,start,end):
    if start>end:
        return 
    mid = (start+end)//2
    temp = Node(arr[mid])
    temp.left = buildBST(arr,start,mid-1)
    temp.right = buildBST(arr,mid+1,end)
    return temp
 
def binaryToBST(root):
    arr = []
    preorder(root,arr)
    arr.sort()
    return buildBST(arr,0,len(arr)-1)
