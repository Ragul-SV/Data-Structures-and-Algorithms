def maxPathSum(root,cursum,maxsum,mini,minval):
    if root:
        cursum+=(root.data)
        if not root.left and not root.right:
            maxsum.append(cursum)
            minval.append(min(mini,root.data))
            return
        maxPathSum(root.left,cursum,maxsum,min(mini,root.data),minval)
        maxPathSum(root.right,cursum,maxsum,min(mini,root.data),minval)
        
def maxRootToLeafPathSum(root):
    maxsum = []
    minval = []
    maxPathSum(root,0,maxsum,2**31,minval)
    res = -2**31
    for i in range(len(maxsum)):
        res = max(res,max(maxsum[i],maxsum[i]-2*minval[i]))
    return res
