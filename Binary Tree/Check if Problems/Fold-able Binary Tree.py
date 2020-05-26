def IsFoldable(root):
    if not root:
        return True
    q =  [root]
    curnode = q.pop(0)
    if not curnode.left and curnode.right:
        return False
    elif not curnode.right and curnode.left:
        return False
    elif curnode.left and curnode.right:
        q.append(curnode.left)
        q.append(curnode.right)
        while q:
            r = q.pop(0)
            l = q.pop(0)
            if not l.left and not r.right and not l.right and not r.left:
                continue
            elif l.left and r.right and not l.right and not r.left:
                q.append(l.left)
                q.append(r.right)
            elif not l.left and not r.right and l.right and r.left:
                q.append(l.right)
                q.append(r.left)
            elif l.left and r.right and l.right and r.left:
                q.append(l.left)
                q.append(r.right)
                q.append(l.right)
                q.append(r.left)
            else:
                return False
    return True
