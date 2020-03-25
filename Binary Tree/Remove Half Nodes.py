def RemoveHalfNodes(root): 
    if root:
        if root.left and not root.right:
            return RemoveHalfNodes(root.left)
        if not root.left and root.right:
            return RemoveHalfNodes(root.right)
        else:
            root.left = RemoveHalfNodes(root.left)
            root.right = RemoveHalfNodes(root.right)
        return root
