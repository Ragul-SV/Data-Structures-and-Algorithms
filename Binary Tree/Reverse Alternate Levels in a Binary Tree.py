def levelorder(root,level,d):
    if root:
        if level%2!=0:
            try:
                d[level].append(root)
            except:
                d[level] = [root]
        levelorder(root.left,level+1,d)
        levelorder(root.right,level+1,d)
        
def reverseAlternate(root):
    d = dict()
    levelorder(root,0,d)
    for arr in d.values():
        n = len(arr)
        for i in range(n//2):
            arr[i].data,arr[n-i-1].data = arr[n-i-1].data,arr[i].data
