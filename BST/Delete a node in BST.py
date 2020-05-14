def deletenode(root,key):
	if not root:
		return root
	
	if root.data<key:
		root.left = deletenode(root.left)
	elif root.data>key:
		root.right = deletenode(root.right)
	else:
		if not root.left:
			temp = root.right
			root = None
			return temp
		elif nor root.right:
			temp = root.left
			root = None
			return temp
		curnode = root.right
		while not curnode.left:
			curnode = curnode.left
		temp = curnode
		root.data = temp.data
		root.right = deletenode(root.right,temp.data)
	return root
