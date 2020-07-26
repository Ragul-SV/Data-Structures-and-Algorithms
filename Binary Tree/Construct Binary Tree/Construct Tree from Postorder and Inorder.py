#----------------------------------------------------------METHOD 1-----------------------------------------------------------------#
def build(inorder,d,postorder,l,h,postindex):
    if l>h:
        return None
    root = Node(postorder[postindex[0]])
    postindex[0]+=1
    if l==h:
        return root
    i = d[root.data]
    if i<=h:
        root.right = build(inorder,d,postorder,i+1,h,postindex)
        root.left = build(inorder,d,postorder,l,i-1,postindex)
    return root
        
def buildTree(In, post, n):
    inorder = list(reversed(In))
    postorder = list(reversed(post))
    postindex = [0]
    d = dict()
    for i in range(n):
        d[In[i]] = i
    return build(In,d,post,0,n-1,postindex)
    
#---------------------------------------------------------METHOD 2-------------------------------------------------------------------#
def build(inorder,postorder,l,h,postindex):
    if l>h:
        return None
    root = Node(postorder[postindex[0]])
    preindex[0]-=1
    if l==h:
        return root
    i = d[root.data]
    if i<=h:
        root.right = build(inorder,postorder,i+1,h,postindex)
        root.left = build(inorder,postorder,l,i-1,postindex)
    return root
        
def buildTree(In, post, n):
    postindex = [n-1]
    d = dict()
    for i in range(n):
        d[In[i]] = i
    return build(In,post,0,n-1,postindex)
