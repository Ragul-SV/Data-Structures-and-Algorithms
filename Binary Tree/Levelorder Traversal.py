#---------------------------------------------------------Recursive------------------------------------------------------#
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
    
    h = height(root)
    
    for i in range(h):
        printlevel(root,i)
    
    #------------------------------------------------------Iterative----------------------------------------------------------#
    
    s = []
    q = [root]
    while q:
        curnode = q.pop(0)
        print(curnode.data,end=" ")
        if curnode.left:
            q.append(curnode.left)
        if curnode.right:
            q.append(curnode.right)
