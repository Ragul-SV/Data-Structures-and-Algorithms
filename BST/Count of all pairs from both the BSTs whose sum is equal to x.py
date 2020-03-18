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
