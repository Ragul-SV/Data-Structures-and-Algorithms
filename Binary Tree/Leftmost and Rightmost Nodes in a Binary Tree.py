def printCorner(root):
    q = [root]
    while q:
        n = len(q)
        for i in range(n):
            curnode = q.pop(0)
            if i==0 or i==n-1:
                print(curnode.data,end=" ")
            if curnode.left:
                q.append(curnode.left)
            if curnode.right:
                q.append(curnode.right)
