#----------------------------------------------O(M*N)-----------------------------------------------------------------------------#
def isSame(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data==root2.data:
        l = isSame(root1.left,root2.left)
        r = isSame(root1.right,root2.right)
        return l and r
    return False

def isSubTree(root1, root2):
    if not root1:
        return False
    l = isSubTree(root1.left,root2)
    r = isSubTree(root1.right,root2)
    return isSame(root1,root2) or l or r
#--------------------------------------------------O(N)-----------------------------------------------------------------------#
class Node:
	def __init__(self,value):
		self.data = value
		self.left = self.right = None
	
def storeinorder(root,arr):
	if not root:
		arr.append('$')
	storeinorder(root.left,arr)
	arr.append(root.data)
	storeinorder(root.right,arr)
	
def storepreorder(root,arr):
	if not root:
		arr.append('$')
	arr.append(root.data)
	storepreorder(root.left,arr)
	storepreorder(root.right,arr)	
	
def isSubtree(T,S):
	if not S:
		return True
	if not T:
		return False
	inT = []
	inS = []
	storeinorder(T,inT)
	storeinorder(S,inS)
	inT = "".join(inT)
	inS = "".join(inS)
	if inT not in inS:
		return False
	preT = []
	preS = []
	storepreorder(T,preT)
	storepreorder(S,preS)
	preT = "".join(preT)
	preS = "".join(preS)
	return preT in preS
