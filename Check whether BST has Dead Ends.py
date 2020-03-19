def checkBST(root,mini,maxi):
    if root==None:
        return True
    if maxi-mini == 0:
        return False
    return checkBST(root.left,mini,root.data-1) and checkBST(root.right,root.data+1,maxi)

def isdeadEnd(root):
    # Code here
    int_min = 1
    int_max = 2**31
    return not checkBST(root,int_min,int_max)
