# A O(n) program for construction of BST from preorder traversal 
 
INT_MIN = -2**31
INT_MAX = 2**31
 
class Node: 
 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
 
def constructTreeUtil(pre, preIndex, key, min, max, size): 
 
	if(preIndex[0] >= size): 
		return None
 
	root = None
 
	if(key > min and key < max): 
 
		root = Node(key) 
		preIndex[0]+=1
 
		if preIndex[0] < size: 
 
			root.left = constructTreeUtil(pre, preIndex,
						pre[preIndex[0]], min, key, size) 
 
			root.right = constructTreeUtil(pre, preIndex,
					pre[preIndex[0]], key, max, size) 
	return root 
 
def constructTree(pre): 
	preIndex = [0]
	size = len(pre) 
	return constructTreeUtil(pre, preIndex, pre[0], INT_MIN, INT_MAX, size) 
 
def printInorder(node): 
 
	if node is None: 
		return
	printInorder(node.left) 
	print(node.data,end=" ")
	printInorder(node.right) 
 
pre = [10, 5, 1, 7, 40, 50] 
root = constructTree(pre) 
 
print("Inorder traversal of the constructed tree: ")
printInorder(root) 
