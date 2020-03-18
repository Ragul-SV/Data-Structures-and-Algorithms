def getCountOfNode(root,l,h):
    ##Your code here
    if not root:
        return 0
    if root.data >=l and root.data<=h:
        return 1+getCountOfNode(root.left,l,h)+getCountOfNode(root.right,l,h)
    elif root.data<l:
        return getCountOfNode(root.right,l,h)
    elif root.data>h:
        return getCountOfNode(root.left,l,h)
