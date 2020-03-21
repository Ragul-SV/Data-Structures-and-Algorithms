INT_MIN = -2**31
INT_MAX = 2**31

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
     
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
    
def inorder(root,arr):
    if root:
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
    
t = int(input())
for i in range(t):
    size = int(input())
    pre = list(map(int,input().strip().split()))
    arr = []
    inorder(constructTree(pre,size),arr)
    # print(arr)
    # print(pre)
    if arr==sorted(arr) and len(arr)==len(pre):
        print(1)
    else:
        print(0)
    
