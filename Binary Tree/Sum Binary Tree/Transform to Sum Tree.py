def toSumTree(root) :
    if not root:
        return 0
    l = toSumTree(root.left)
    r = toSumTree(root.right)
    old_val = root.data
    root.data  = l+r
    return root.data + old_val
