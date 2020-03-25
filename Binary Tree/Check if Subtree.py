def isSame(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data==root2.data:
        l = isSame(root1.left,root2.left)
        r = isSame(root1.right,root2.right)
        return l and r
    return False

def isSubTree(root1, root2):
    if not root1:
        return False
    l = isSubTree(root1.left,root2)
    r = isSubTree(root1.right,root2)
    return isSame(root1,root2) or l or r
