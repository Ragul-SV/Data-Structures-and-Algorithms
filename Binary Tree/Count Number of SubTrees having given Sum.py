def subsum(root):
    if not root:
        return 0
    return root.data + subsum(root.left) + subsum(root.right)
    
def count(root,x):
    if(subsum(root)==x):
        return 1
    return 0
    
def countSubtreesWithSumX(root ,x):
    if not root:
        return 0
    return count(root,x) + countSubtreesWithSumX(root.left,x) + countSubtreesWithSumX(root.right,x)
