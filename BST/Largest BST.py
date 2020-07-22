class info:
    def __init__(self,size,mini,maxi,ans,isBST):
        self.size = size
        self.mini = mini
        self.maxi = maxi
        self.ans = ans
        self.isBST = isBST

# Return the size of the largest sub-tree which is also a BST
def largest(root):
    if not root:
        return info(0,2**31,-2**31,1,True)
    if not root.left and not root.right:
        return info(1,root.data,root.data,1,True)
    l = largest(root.left)
    r = largest(root.right)
    temp = info(0,0,0,0,True)
    temp.size = l.size+r.size+1
    temp.mini = min(l.mini,min(root.data,r.mini))
    temp.maxi = max(l.maxi,max(root.data,r.maxi))
    if l.isBST and r.isBST and l.maxi<root.data and r.mini>root.data:
        temp.ans = temp.size
        temp.isBST = True
        return temp
    temp.ans = max(l.ans,r.ans)
    temp.isBST = False
    return temp

def largestBst(root):
    return largest(root).ans
