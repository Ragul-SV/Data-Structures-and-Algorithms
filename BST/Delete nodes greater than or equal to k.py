def deleteNode(root, x):
    # Code here
    if not root:
        return
    if root.data==x:
        return root.left
    elif root.data<x:
        root.right = deleteNode(root.right,x)
        return root
    elif root.data>x:
        return deleteNode(root.left,x)
