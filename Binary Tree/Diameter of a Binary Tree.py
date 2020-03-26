def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def diameter(root):
    if not root:
        return 0
    return max(diameter(root.left),diameter(root.right),1+height(root.left)+height(root.right))
