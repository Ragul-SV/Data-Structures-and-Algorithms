def maxdiff(root,res):
    if not root:
        return 2**31
    if not root.left and not root.right:
        return root.data
    mini = min(maxdiff(root.left,res),maxdiff(root.right,res))
    res[0] = max(res[0],root.data - mini)
    return min(mini,root.data)
    
def maxDiff(root):
    res = [-2**31]
    maxdiff(root,res)
    return res[0]
