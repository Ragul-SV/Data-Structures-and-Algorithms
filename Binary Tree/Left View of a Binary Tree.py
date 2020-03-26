#-----------------------------------------------------METHOD 1--------------------------------------------------------------------#
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left),height(root.right))
    
def printLeftView(root,level,flag):
    if root and not flag[0]:
        if level==0:
            if flag[0] == False:
                print(root.data,end=" ")
                flag[0] = True
        printLeftView(root.left,level-1,flag)
        printLeftView(root.right,level-1,flag)
    
def LeftView(root):
    h = height(root)
    for i in range(h):
        flag = [False]
        printLeftView(root,i,flag)

#-----------------------------------------------------METHOD 2--------------------------------------------------------------------#
def printLeftView(root,level,d):
    if root:
        d[level] = root.data
        printLeftView(root.right,level+1,d)
        printLeftView(root.left,level+1,d)
    
def LeftView(root):
    d = dict()
    printLeftView(root,0,d)
    for i in d.values():
        print(i,end=" ")
