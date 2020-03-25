def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def sumOfLongRootToLeafPath(root):
    if root:
        if height(root.left)>height(root.right):
            return root.data + sumOfLongRootToLeafPath(root.left)
        if height(root.right)>height(root.left):
            return root.data + sumOfLongRootToLeafPath(root.right)
        return root.data + max(sumOfLongRootToLeafPath(root.left),sumOfLongRootToLeafPath(root.right))
    return 0
