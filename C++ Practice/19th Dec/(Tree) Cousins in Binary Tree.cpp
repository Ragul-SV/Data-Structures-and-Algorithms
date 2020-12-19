bool isSibling(TreeNode* root,int x,int y)
    {
        if(root==NULL)return false;
        if(root->left!=NULL && root->right!=NULL)
        return (root->left->val==x && root->right->val==y) || (root->left->val==y && root->right->val==x) || isSibling(root->left,x,y) || isSibling(root->right,x,y);
        return isSibling(root->left,x,y) || isSibling(root->right,x,y);
    }
    
    void depth(TreeNode* root,int x,int d,int &res)
    {
        if(root==NULL)return;
        if(root->val==x)res = d;;
        depth(root->left,x,d+1,res);
        depth(root->right,x,d+1,res);
    }
    
    bool isCousins(TreeNode* root, int x, int y) {
        if(x==y)return false;
        if(root==NULL)return false;
        int xd,yd;
        depth(root,x,1,xd);
        depth(root,y,1,yd);
        return xd==yd && !isSibling(root,x,y);
    }
