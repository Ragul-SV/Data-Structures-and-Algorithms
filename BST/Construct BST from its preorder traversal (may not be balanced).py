#code
def insert(root,node):
    if root:
        if node.data<root.data:
            root.left = insert(root.left,node)
        else:
            root.right = insert(root.right,node)
        return root
    else:
        return node
 
def preorderBST(arr,n):
    root = Node(arr[0])
    for i in range(1,n):
        node = Node(arr[i])
        insert(root,node)
    return root
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
 
class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
 
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        root = preorderBST(arr,n)
        inorder(root)
        print()
