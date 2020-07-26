#----------------------------------------------O(N)----There are total three traversals of the tree------------------------------------------------------------#
def isSibling(root,a,b):
    if not root:
        return False
    return (root.left.data==a and root.right.data==b) or (root.left.data==b and root.right.data==a) or isSibling(root.left,a,b) or isSibling(root.right,a,b)
        
    
def vertical(root,value,level):
    if not root:
        return
    if root.data==value:
        return level
    return vertical(root.left,value,level+1) or vertical(root.right,value,level+1)

def isCousin(root, a, b):
    if a==b:
        return
    return (vertical(root,a,1)==vertical(root,b,1)) and not isSibling(root,a,b)
