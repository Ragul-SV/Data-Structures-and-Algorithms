def PreOrder(root):

    # Recursive
    
    if root:
        print(root.data,end=" ")
        PreOrder(root.left)
        PreOrder(root.right)
        
    # Iterative    
        
    s = []
    s.append(root)
    while s:
        cur = s.pop()
        if cur:
           print(cur.data,end=" ")
           s.append(cur.right)
           s.append(cur.left)
