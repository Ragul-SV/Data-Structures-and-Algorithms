def findlevel(root,level,arr):
    if root:
        if not root.left and not root.right:
            arr.append(level)
        findlevel(root.left,level+1,arr)
        findlevel(root.right,level+1,arr)

def check(node):
    arr = []
    flevel = findlevel(root,0,arr)
    return len(set(arr))==1
