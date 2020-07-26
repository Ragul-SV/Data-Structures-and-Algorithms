def alternate(root,level,D):
    if root:
        try:
            d[level].append(root.data)
        except:
            d[level] = [root.data]
        alternate(root.left,level+1,d)
        alternate(root.right,level+1,d)

def printExtremeNodes(root):
    # Code here
    d = dict()
    alternate(root,0,d)
    for i,value in enumerate(d.values()):
        if i%2==0:
            print(value[-1],end=" ")
        else:
            print(value[0],end=" ")
