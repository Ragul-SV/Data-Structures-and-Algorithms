def getk():
    return inorder.k
 
def decrementk():
    inorder.k -= 1
 
def inorder(root,k):
    if root:
        inorder(root.right,getk())
        decrementk()
        if getk()==0:
            print(root.data)
        inorder(root.left,getk())
 
def kthLargest(root, k):
    inorder.k = k
    inorder(root,k)
