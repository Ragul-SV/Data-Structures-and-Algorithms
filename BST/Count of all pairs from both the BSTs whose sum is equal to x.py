#---------------------METHOD1-----O(N1*H2)----N1:Number of Nodes in First BST----H2:Height of Second BST--------------------------------#
def search(root,val):
    flag = False
    if root and (root.data==val or search(root.left,val) or search(root.right,val)):
        flag = True
    return flag
 
def countPairs(root1, root2, x):
    if not root1:
        return 0
    elif search(root2,x - root1.data):
        return 1 + countPairs(root1.left,root2,x) + countPairs(root1.right,root2,x)
    else:
        return countPairs(root1.left,root2,x) + countPairs(root1.right,root2,x)
#---------------------METHOD2-----O(N)--------------------------------------------------------------------------------------------------#
class Node:
	def __init__(self,value):
		self.data = value
		self.left = self.right = None
	
def countPairs(root1,root2,x):
	if not root1 or not root2:
		return 0
	st1 = []
	st2 = []
	count = 0
	while True:
		while root1:
			st1.append(root1)
			root1 = root1.left
		
		while root2:
			st2.append(root2)
			root2 = root2.right
		
		if not st1 or not st2:
			break
		
		top1 = st1[-1]
		top2 = st2[-1]
		if (top1.data + top2.data) == x:
			count+=1
			st1.pop()
			st2.pop()
			root1 = top1.right
			root2 = top2.left
		elif if (top1.data + top2.data) < x:
			st1.pop()
			root1 = top1.right
		else:
			st2.pop()
			root2 = top2.left
	return count
