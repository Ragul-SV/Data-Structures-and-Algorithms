Node* construct(int pre[], int preMirror[], int l, int h, int &preindex)
{
    if(l>h) return NULL;
    Node* root = new Node(pre[preindex++]); 
    if(l==h) return root;
    int i=l;
    for(i;i<=h;i++)
    {
        if(pre[preindex] == preMirror[i]) break;
    }
    if(i<=h)
    {
        root->left = construct(pre,preMirror,i,h,preindex);
        root->right = construct(pre,preMirror,l+1,i-1,preindex);
    }
    return root;
}

Node* constructBinaryTree(int pre[], int preMirror[], int size)
{
    int index = 0;
    return construct(pre,preMirror,0,size-1,index);
}
