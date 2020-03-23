def path(root,st):
    if root:
        if not root.left and not root.right:
            print(st + str(root.data) + " #",end="")
        else:
            st += str(root.data) + " "
            path(root.left,st)
            path(root.right,st)
    
def printPath(root):
    st = ""
    path(root,st)
