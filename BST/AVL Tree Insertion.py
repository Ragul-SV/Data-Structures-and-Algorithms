class Node:
	def __init__(self,val):
		self.data = val
		self.left = None
		self.right = None
		self.height = 1
		
def insert(root,val):
	if root==None:
		return Node(val)
	if val<root.data:
		root.left = insert(root.left,val)
	elif val>root.data:
		root.right = insert(root.right,val)
		
	root.height = 1+max(height(root.left),height(root.right))
	balance = getBalance(root)
	
	if balance>1 and val<root.left.data:
		return rightRotate(root)
	if balance>1 and val>root.left.data:
		root.left = leftRotate(root.left)
		return rightRotate(root)
	if balance<-1 and val>root.right.data:
		return leftRotate(root)
	if balance<-1 and val<root.right.data:
		root.right = rightRotate(root.right)
		return leftRotate(root)
	
	return root
	
def leftRotate(z):
	y = z.right
	temp = y.left
	
	y.left = z
	z.right = temp
	
	z.height = 1+max(height(z.left),height(z.right))
	y.height = 1+max(height(y.left),height(y.right))
	
	return y
	
def rightRotate(z):
	y = z.left
	temp = y.right
	
	y.right = z
	z.left = temp
	
	z.height = 1+max(height(z.left),height(z.right))
	y.height = 1+max(height(y.left),height(y.right))
	
	return y
	
def getBalance(root):
	if root==None:
		return 0
	return height(root.left) - height(root.right)
		
def height(root):
	if root==None:
		return 0
	return root.height
	
def preorder(root):
	if root:
		preorder(root.left)
		print(root.data,end=" ")
		preorder(root.right)
	
n = int(input())
arr = list(map(int,input().strip().split()))
root = None
for i in range(0,n):
	root = insert(root,arr[i])
print(height(root)-1)
preorder(root)
print()
