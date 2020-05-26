int find(Node *root,int k, int node, int &count, int &res)
{
    if(root!=NULL)
    {
        if(root->data==node)
        {
            return 1;
        }
        if(find(root->left,k,node,count,res)||find(root->right,k,node,count,res))
        {
            count++;
            if(count==k) res = root->data;
            return 1;
        }
    }
    return 0;
}

int kthAncestor(Node *root, int k, int node)
{
    int res = -1,count = 0;
    find(root,k,node,count,res);
    return res;
}
