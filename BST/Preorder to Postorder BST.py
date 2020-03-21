INT_MIN = -2**31
INT_MAX = 2**31
 
class Node: 
 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
 
def getpreindex():
    return preBST.preindex;
    
def incrementpreindex():
    preBST.preindex+=1

def preBST(pre,key,min,max,size):
	if getpreindex()>=size:
		return None
	root = None
	if key>min and key<max:
		root = Node(key) 
		incrementpreindex()
		if getpreindex() < size: 
			root.left = preBST(pre, pre[getpreindex()], min, key, size) 
		if getpreindex() < size:
			root.right = preBST(pre, pre[getpreindex()], key, max, size) 
	return root

def constructTree(pre,size): 
	preBST.preindex = 0
	return preBST(pre, pre[preBST.preindex], INT_MIN, INT_MAX, size) 
 
def postorder(node): 
 
	if node is None: 
		return
	postorder(node.left) 
	postorder(node.right) 
	print(node.data,end=" ")
 

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        pre = list(map(int,input().strip().split()))
        root = constructTree(pre,n)
        postorder(root)
        print()
