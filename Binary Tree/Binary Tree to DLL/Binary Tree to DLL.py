def inorder(root,arr): 
    if root:
        inorder(root.left,arr)
        arr.append(Node(root.data))
        inorder(root.right,arr)
        
def btodll(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.right = Node(arr[i])
        prev = temp
        temp = temp.right
        temp.left = prev
    return head
    
def bToDLL(root):
    # do Code here
    arr = [] 
    inorder(root,arr)
    return btodll(arr)
