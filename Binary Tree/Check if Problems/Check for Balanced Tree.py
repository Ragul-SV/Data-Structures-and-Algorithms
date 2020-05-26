#----------------------METHOD1-----------------O(N^2)-------------------------------------------------------------------#
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
 
def isBalanced(root):
    if not root:
        return True
    return (abs(height(root.left)-height(root.right))<=1) and isBalanced(root.left) and isBalanced(root.right) 
#----------------------METHOD2-----------------O(N)---------------------------------------------------------------------#
def dfsheight(root):
    if not root:
        return 0
    lh = dfsheight(root.left)
    if lh == -1:
        return -1
    rh = dfsheight(root.right)
    if rh == -1:
        return -1
    if abs(lh-rh)>1:
        return -1
    return 1 + max(lh,rh)

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return dfsheight(root)!=-1
