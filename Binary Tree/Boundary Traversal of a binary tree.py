class Node: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
 
def printLeaves(root):
    if root:
        printLeaves(root.left)
        if not root.left and not root.right:
            print(root.data,end=" ")
        printLeaves(root.right)
 
def printBoundaryLeft(root):
    if root:
        if root.left:
            print(root.data,end=" ")
            printBoundaryLeft(root.left)
        elif root.right:
            print(root.data,end=" ")
            printBoundaryLeft(root.right)
 
def printBoundaryRight(root):
    if root:
        if root.right:
            printBoundaryRight(root.right)
            print(root.data,end=" ")
        elif root.left:
            printBoundaryRight(root.left)
            print(root.data,end=" ")
 
def printBoundaryView(root):
    if root:
        print(root.data,end=" ")
        printBoundaryLeft(root.left)
        printLeaves(root.left)
        printLeaves(root.right)
        printBoundaryRight(root.right)
 
def buildTree(s):
	if len(s)==0 or s[0]=="N":
		return None
 
	tree = list(map(str,s.strip().split()))
	root = Node(int(tree[0]))
	size = 0
	q = []
	q.append(root)
	size = size+1
	i=1
	while size>0 and i<len(tree):
		curnode = q[0]
		q.pop(0)
		size = size-1
 
		curval = tree[i]
		if curval!="N":
			curnode.left = Node(int(curval))
			q.append(curnode.left)
			size=size+1
		i+=1
 
		if i>=len(tree):
			break
 
		curval = tree[i]
		if curval!="N":
			curnode.right = Node(int(curval))
			q.append(curnode.right)
			size=size+1
		i=i+1
 
	return root
 
if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
  		s = input()
  		root = buildTree(s)
  		printBoundaryView(root)
  		print()
