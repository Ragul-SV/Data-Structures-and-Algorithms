def symmetric(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data!=root2.data:
        return False
    return symmetric(root1.left,root2.right) and symmetric(root1.right,root2.left)
    
def isSymmetric(root):
    if not root:
        return True
    return symmetric(root.left,root.right)
