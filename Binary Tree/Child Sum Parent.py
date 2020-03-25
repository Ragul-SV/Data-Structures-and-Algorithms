def isSumProperty(root):
    if root:
        if root.left and root.right:
            if root.data != root.left.data+root.right.data:
                return 0
        elif root.left and not root.right:
            if root.data != root.left.data:
                return 0
        elif not root.left and root.right:
            if root.data != root.right.data:
                return 0
        return isSumProperty(root.left) and isSumProperty(root.right)
    return 1
