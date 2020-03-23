def reversePrint(root):
    s = []
    q = [root]
    while q:
        curnode = q.pop(0)
        s.append(curnode.data)
        if curnode.right:
            q.append(curnode.right)
        if curnode.left:
            q.append(curnode.left)
            
    while s:
        print(s.pop(),end=" ")
