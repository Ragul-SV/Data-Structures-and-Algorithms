int diameter(TreeNode* root,int &res)
    {
        if(root==NULL)return 0;
        int l = diameter(root->left,res);
        int r = diameter(root->right,res);
        res = max(res,l+r+1);
        return max(l,r)+1;
    }
    
    int diameterOfBinaryTree(TreeNode* root) {
        int res = 1;
        diameter(root,res);
        return res-1;
    }
