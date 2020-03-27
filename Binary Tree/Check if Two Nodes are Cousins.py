def vertical(root,value,level,depth,arr):
    if root:
        if root.left and root.left.data == value:
            arr.append(level+1)
            arr.append(root)
            arr.append("L")
            arr.append(root.left)
        elif root.right and root.right.data == value:
            arr.append(level+1)
            arr.append(root)
            arr.append("R")
            arr.append(root.right)
        vertical(root.left,value,level+1,depth-1,arr)
        vertical(root.right,value,level+1,depth+1,arr)

def isCousin(root,a,b):
    arr1 = []
    vertical(root,a,0,0,arr1)
    arr2 = []
    vertical(root,b,0,0,arr2)
    # print(arr1[0],arr1[1].data,arr1[2],arr1[3].data)
    # print(arr2[0],arr2[1].data,arr2[2],arr2[3].data)
    if not arr1 or not arr2:
        return False
    elif arr1[0]==arr2[0]:
        if arr1[1]==arr2[1]:
            return False
        return True
    else:
        return False
