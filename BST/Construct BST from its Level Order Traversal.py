def insert(root,node):
    if root:
        if node.data<root.data:
            if root.left==None:
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right==None:
                root.right = node
            else:
                insert(root.right,node)
 
##Complete this function
def constructBst(arr,n):
    #Your code here
    root = Node(arr[0])
    for i in range(1,n):
        node = Node(arr[i])
        insert(root,node)
    return root
