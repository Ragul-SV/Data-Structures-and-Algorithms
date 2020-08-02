def morris_inorder(root):
	current = root
	while current!=None:
		if current.left!=None:
			print(current.data)
			current = current.right
		else:
			temp = current.left
			while temp.right!=None and temp.right!=current:
				temp = temp.right
			if temp.right==None:
				temp.right = current
				current = current.left
			else:
				temp.right = None
				print(current.data)
				current = current.right
