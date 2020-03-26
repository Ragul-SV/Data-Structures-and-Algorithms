#------------------------------------------------------METHOD 1--------------------------------------------------------------#
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def printRightView(root,level,flag):
    if root and not flag[0]:
        if level==0:
            if flag[0] == False:
                print(root.data,end=" ")
                flag[0] = True
        printRightView(root.right,level-1,flag)
        printRightView(root.left,level-1,flag)
    
def rightView(root):
    h = height(root)
    for i in range(h):
        flag = [False]
        printRightView(root,i,flag)
        
#-----------------------------------------------------METHOD 2-----------------------------------------------------------------#
def printRightView(root,level,d):
    if root:
        d[level] = root.data
        printRightView(root.left,level+1,d)
        printRightView(root.right,level+1,d)
    
def rightView(root):
    d = dict()
    printRightView(root,0,d)
    for i in d.values():
        print(i,end=" ")
