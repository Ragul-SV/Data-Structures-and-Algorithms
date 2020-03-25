def sumtree(root):
    if not root:
        return 0
    return root.data + sumtree(root.left) + sumtree(root.right)
    
def isSumTree(root):
    # Code here
    if not root:
        return True
    if not root.left and not root.right:
        return True
    return (root.data==(sumtree(root.left)+sumtree(root.right))) and isSumTree(root.left) and isSumTree(root.right)
