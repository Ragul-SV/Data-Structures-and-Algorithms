#---------TOP DOWN APPROACH------O(N^2)-----------WORST CASE FOR SKEWED TREE-----------------------------------------------#
def sumtree(root):
    if not root:
        return 0
    return root.data + sumtree(root.left) + sumtree(root.right)
    
def isSumTree(root):
    # Code here
    if not root:
        return True
    if not root.left and not root.right:
        return True
    return (root.data==(sumtree(root.left)+sumtree(root.right))) and isSumTree(root.left) and isSumTree(root.right)
#---------BOTTOM UP APPROACH------O(N)-------------------------------------------------------------------------------------#
def isLeaf(root):
    return not root.left and not root.right
    
def isSumTree(root):
    if not root or isLeaf(root):
        return True
    if root.left and root.right:
        if not root.left:
            ls = False
        elif isLeaf(root.left):
            ls = root.left.data
        else:
            ls = 2*(root.left.data)
        
        if not root.right:
            rs = False
        elif isLeaf(root.right):
            rs = root.right.data
        else:
            rs = 2*(root.right.data)
        
        return root.data == ls+rs
    return False
