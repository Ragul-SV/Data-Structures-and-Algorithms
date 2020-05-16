#--------------------------------------TOP DOWN APPROACH------------O(N^2)----------------------------------------------#
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))

def diameter(root):
    if not root:
        return 0
    return max(diameter(root.left),diameter(root.right),1+height(root.left)+height(root.right))
#--------------------------------------BOTTOM UP APPROACH------------O(N)----------------------------------------------#
class Height:
    def __init__(self):
        self.h = 0
        
def diameterUtil(root,height):
    lh = Height()
    rh = Height()
    if not root:
        height.h = 0
        return 0
    ldiameter = diameterUtil(root.left,lh)
    rdiameter = diameterUtil(root.right,rh)
    height.h = 1 + max(lh.h,rh.h)
    return max(1+lh.h+rh.h,max(ldiameter,rdiameter))
    
def diameter(root):
    height = Height()
    return diameterUtil(root,height)
