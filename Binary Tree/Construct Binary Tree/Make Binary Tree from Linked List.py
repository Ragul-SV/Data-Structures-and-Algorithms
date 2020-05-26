def convert(head):
    q = []
    node = Tree(head.data)
    q = [node]
    while q:
        size = len(q)
        for i in range(size):
            curnode = q.pop(0)
            if head.next:
                head = head.next
                temp = Tree(head.data)
                curnode.left = temp
                q.append(temp)
            if head.next:
                head = head.next
                temp = Tree(head.data)
                curnode.right = temp
                q.append(temp)
    return node
