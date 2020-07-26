#-------------------------------O(N^2)----------------------------------------------#
Node* buildTree(int in[],int pre[], int l, int h)
{
    if(l>h) return NULL;
    Node* root = new Node(pre[preIndex++]);
    if(l==h) return root;
    int i;
    for(i=l;i<=h;i++)
    {
        if(root->data==in[i]) break;
    }
    if(i<=h)
    {
        root->left = buildTree(in,pre,l,i-1);
        root->right = buildTree(in,pre,i+1,h);
    }
    return root;
}

/* Python using Hash Table to Store inorder elements index O(N)
def build(inorder,d,preorder,preIndex,l,r):
    if l>r:
        return None
    root = Node(preorder[preIndex[0]])
    preIndex[0]+=1
    if l==r:
        return root
    i = d[root.data]
    if i<=r:
        root.left = build(inorder,d,preorder,preIndex,l,i-1)
        root.right = build(inorder,d,preorder,preIndex,i+1,r)
    return root
            
    
def buildtree(inorder, preorder, n):
    preIndex = [0]
    d = dict()
    for i in range(n):
        d[inorder[i]] = i
    return build(inorder,d,preorder,preIndex,0,n-1)
*/
