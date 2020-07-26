Node* construct(int pre[], int preMirror[],unordered_map<char,int> mp, int l, int h, int &preindex)
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
        root->left = construct(pre,preMirror,mp,i,h,preindex);
        root->right = construct(pre,preMirror,mp,l+1,i-1,preindex);
    }
    return root;
}

Node* constructBinaryTree(int pre[], int preMirror[], int size)
{
    int index = 0;
    unordered_map<char,int> mp;
    for(int i=0;i<size;i++) mp[preMirror] = i;
    return construct(pre,preMirror,mp,0,size-1,index);
}
