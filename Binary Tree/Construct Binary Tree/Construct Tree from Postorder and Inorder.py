#----------------------------------------------------------METHOD 1-----------------------------------------------------------------#
def build(inorder,postorder,l,h,preindex):
    if l>h:
        return None
    root = Node(postorder[preindex[0]])
    preindex[0]+=1
    if l==h:
        return root
    i = l
    for i in range(l,h+1):
        if root.data==inorder[i]:
            break
    if i<=h:
        root.right = build(inorder,postorder,i+1,h,preindex)
        root.left = build(inorder,postorder,l,i-1,preindex)
    return root
        
def buildTree(In, post, n):
    inorder = list(reversed(In))
    postorder = list(reversed(post))
    preindex = [0]
    return build(In,post,0,n-1,preindex)
    
#---------------------------------------------------------METHOD 2-------------------------------------------------------------------#
def build(inorder,postorder,l,h,preindex):
    if l>h:
        return None
    root = Node(postorder[preindex[0]])
    preindex[0]-=1
    if l==h:
        return root
    i = l
    for i in range(l,h+1):
        if root.data==inorder[i]:
            break
    if i<=h:
        root.right = build(inorder,postorder,i+1,h,preindex)
        root.left = build(inorder,postorder,l,i-1,preindex)
    return root
        
def buildTree(In, post, n):
    preindex = [n-1]
    return build(In,post,0,n-1,preindex)
