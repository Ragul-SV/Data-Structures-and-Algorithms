def InOrder(root):

    # Recursive
    
    if root:
        InOrder(root.left)
        print(root.data,end=" ")
        InOrder(root.right)
        
    # Iterative 
    
    s = []
    cur = root
    
    while s or cur:
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            cur = s.pop()
            print(cur.data,end=" ")
            cur = cur.right
