def postOrder(root):
    
    #Recursive
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
        
    #Iterative
    if not root:
        return
    s1 = [root]
    s2 = []
    while s1:
        cur = s1.pop()
        s2.append(cur)
        if cur.left:
            s1.append(cur.left)
        if cur.right:
            s1.append(cur.right)
    while s2:
        print(s2.pop().data,end=" ")
