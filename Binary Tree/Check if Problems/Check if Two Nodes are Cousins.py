#----------------------------------------------O(N)----There are total three traversals of the tree-----------------------------------------------#
def isSibling(root,a,b):
    if not root:
        return False
    return (root.left==a and root.right==b) or (root.left==b and root.right==a) or isSibling(root.left,a,b) or isSibling(root.right,a,b)

def vertical(root,value,level,depth,arr):
    if root:
        if root.left and root.left.data == value:
            arr.append(level+1)
            arr.append(root)
        elif root.right and root.right.data == value:
            arr.append(level+1)
            arr.append(root)
        vertical(root.left,value,level+1,depth-1,arr)
        vertical(root.right,value,level+1,depth+1,arr)

def isCousin(root,a,b):
    arr1 = []
    vertical(root,a,0,0,arr1)
    arr2 = []
    vertical(root,b,0,0,arr2)
    if not arr1 or not arr2:
        return False
    return arr1[0]==arr2[0] and isSibling(root,arr1[1],arr2[1])
