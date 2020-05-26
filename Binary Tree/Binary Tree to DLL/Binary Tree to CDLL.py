def inorder(root,s):
    if root:
        inorder(root.left,s)
        s.append(root.data)
        inorder(root.right,s)
    
def bTreeToClist(root):
    s = []
    inorder(root,s)
    head = Node(s[0])
    h = head
    for i in range(1,len(s)):
        head.right = Node(s[i])
        prev = head
        head = head.right
        head.left = prev
    head.right = h
    h.left = head
    return h
