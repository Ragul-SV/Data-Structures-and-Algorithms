def toSumTree(root) :
    if not root:
        return 0
    curdata = root.data
    l = toSumTree(root.left)
    r = toSumTree(root.right)
    root.data = l+r
    return root.data + curdata
