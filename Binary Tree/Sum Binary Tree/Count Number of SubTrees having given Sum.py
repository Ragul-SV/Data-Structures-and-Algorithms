#-------------------------------TOP DOWN APPROACH--------O(N^2)----------------------------------------------------#
def subsum(root):
    if not root:
        return 0
    return root.data + subsum(root.left) + subsum(root.right)
    
def count(root,x):
    if(subsum(root)==x):
        return 1
    return 0
    
def countSubtreesWithSumX(root ,x):
    if not root:
        return 0
    return count(root,x) + countSubtreesWithSumX(root.left,x) + countSubtreesWithSumX(root.right,x)
#-------------------------------BOTTOM UP APPROACH--------O(N)-----------------------------------------------------#
def subsum(root,c,x):
    if not root:
        return 0
    ls = subsum(root.left,c,x)
    rs = subsum(root.right,c,x)
    s = ls + rs + root.data
    if s==x:
        c[0] += 1
    return s
    
def countSubtreesWithSumX(root,x):
    if not root:
        return 0
    c = [0]
    subsum(root,c,x)
    return c[0]
