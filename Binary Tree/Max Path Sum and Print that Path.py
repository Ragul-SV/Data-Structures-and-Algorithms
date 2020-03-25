def pathsum(root,cursum,maxsum,targetnode):
    if not root:
        return False
    cursum += root.data
    if not root.left and not root.right:
        if cursum>maxsum[0]:
            maxsum[0] = cursum
            targetnode[0] = root
    pathsum(root.left,cursum,maxsum,targetnode)
    pathsum(root.right,cursum,maxsum,targetnode)

def printpath(root,targetnode):
    if not root:
        return False
    if root == targetnode:
        print(root.data,end=" ")
        return True
    if printpath(root.left,targetnode) or printpath(root.right,targetnode):
        print(root.data,end=" ")
        return True
    return False
    
def maxPathSum(root):
    maxsum = [-2**31]
    targetnode = [None]
    pathsum(root,0,maxsum,targetnode)
    print("maxsum: ",maxsum[0])
    printpath(root,targetnode[0])
