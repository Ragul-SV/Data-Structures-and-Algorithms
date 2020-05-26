def construct(pre,preLN,n,index):
    if index[0]>=n:
        return
    if preLN[index[0]]=='L':
        return Node(pre[index[0]])
    root = Node(pre[index[0]])
    index[0]+=1
    root.left = construct(pre,preLN,n,index)
    index[0]+=1 
    root.right = construct(pre,preLN,n,index)
    return root
    
def constructTree(pre, preLN, n):
    index = [0]
    return construct(pre,preLN,n,index)
