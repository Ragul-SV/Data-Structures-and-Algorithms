#---------------TOP DOWN APPROACH-----------------------O(N^2)------------------------------------------------------------------------#
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def sumOfLongRootToLeafPath(root):
    if root:
        if height(root.left)>height(root.right):
            return root.data + sumOfLongRootToLeafPath(root.left)
        if height(root.right)>height(root.left):
            return root.data + sumOfLongRootToLeafPath(root.right)
        return root.data + max(sumOfLongRootToLeafPath(root.left),sumOfLongRootToLeafPath(root.right))
    return 0
#------------------BOTTOM UP APPROACH---------------------O(N)------------------------------------------------------------------------#
def sumOfLongRootToLeafPathUtil(root,s,l,maxs,maxl):
    if not root:
        if l>maxl[0]:
            maxl[0] = l
            maxs[0] = s
        elif l==maxl[0] and s>maxs[0]:
            maxs[0] = s
        return
    sumOfLongRootToLeafPathUtil(root.left,s+root.data,l+1,maxs,maxl)
    sumOfLongRootToLeafPathUtil(root.right,s+root.data,l+1,maxs,maxl)
    
def sumOfLongRootToLeafPath(root):
    if not root:
        return 0
    maxs = [-2**31]
    maxl = [0]
    sumOfLongRootToLeafPathUtil(root,0,0,maxs,maxl)
    return maxs[0]
