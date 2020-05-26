def inorder(root,arr): 
    if root:
        inorder(root.left,arr)
        arr.append(Node(root.data))
        inorder(root.right,arr)
        
def btodll(arr):
    head = arr[0]
    temp = head
    for i in range(1,len(arr)):
        temp.right = arr[i]
        temp = temp.right
        temp.left = arr[i-1]
    return head
    
def bToDLL(root):
    # do Code here
    arr = []
    inorder(root,arr)
    return btodll(arr)
