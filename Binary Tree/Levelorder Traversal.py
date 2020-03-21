def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def printlevel(root,level):
    if root:
        if level==0:
            print(root.data,end=" ")
        printlevel(root.left,level-1)
        printlevel(root.right,level-1)
    
def levelOrder( root ):
    # Code here
    h = height(root)
    
    for i in range(h):
        printlevel(root,i)
