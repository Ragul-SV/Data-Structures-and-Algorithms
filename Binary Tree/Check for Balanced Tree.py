def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
 
def isBalanced(root):
    if not root:
        return True
    return (abs(height(root.left)-height(root.right))<=1) and isBalanced(root.left) and isBalanced(root.right) 
