def toSumTree(root) :
    if not root:
        return 0
    l = toSumTree(root.left)
    r = toSumTree(root.right)
    return l + r + root.data
