#-----------------------------------------------------------METHOD 1-------------------------------------------------------------------#
def zigZagTraversal(root):
    s1 = [root]
    s2 = []
    while s1 or s2:
        while s1:
            curnode = s1.pop()
            print(curnode.data,end=" ")
            if curnode.left:
                s2.append(curnode.left)
            if curnode.right:
                s2.append(curnode.right)
        while s2:
            curnode =s2.pop()
            print(curnode.data,end=" ")
            if curnode.right:
                s1.append(curnode.right)
            if curnode.left:
                s1.append(curnode.left)
#----------------------------------------------------------METHOD 2---------------------------------------------------------------------#                
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
        
def printlevelreverse(root,level):
    if root:
        if level==0:
            print(root.data,end=" ")
        printlevelreverse(root.right,level-1)
        printlevelreverse(root.left,level-1)
    
def zigZagTraversal(root):
    h = height(root)
    for i in range(h):
        if i%2==0:
            printlevel(root,i)
        else:
            printlevelreverse(root,i)
