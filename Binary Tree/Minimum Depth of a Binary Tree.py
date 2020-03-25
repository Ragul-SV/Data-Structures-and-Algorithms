def minDepth(root):
    if not root:
        return 0
    if not root.left and root.right:
        return 1 + minDepth(root.right)
    if root.left and not root.right:
        return 1 + minDepth(root.left)
    return 1 + min(minDepth(root.left),minDepth(root.right)) 
