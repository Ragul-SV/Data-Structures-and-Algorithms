def alternate(root,level,d,flag):
    if root:
        if level%2==0 and flag[level]:
            try:
                d[level].append(root.data)
            except:
                d[level] = [root.data]
        else:
            try:
                d[level].append(root.data)
            except:
                d[level] = [root.data]
        alternate(root.left,level+1,d,flag)
        alternate(root.right,level+1,d,flag)

def printExtremeNodes(root):
    # Code here
    d = dict()
    flag = [True]*100
    alternate(root,0,d,flag)
    for i,value in enumerate(d.values()):
        if i%2==0:
            print(value[-1],end=" ")
        else:
            print(value[0],end=" ")
