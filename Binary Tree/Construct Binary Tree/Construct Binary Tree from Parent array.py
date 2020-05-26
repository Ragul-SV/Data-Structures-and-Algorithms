def createTree(arr,n):
    d = dict()
    for i in range(0,n):
        d[i] = Node(i)
    root = None
    for i in range(0,n):
        if arr[i]==-1:
            root = d[i]
        elif not d[arr[i]].left:
            d[arr[i]].left = d[i]
        elif not d[arr[i]].right:
            d[arr[i]].right = d[i]
    return root
