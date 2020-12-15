void greaterSum(TreeNode* root,int &res)
    {
        if(root->right) greaterSum(root->right,res);
        res = root->val = res+root->val;
        if(root->left) greaterSum(root->left,res);
    }
    
    TreeNode* bstToGst(TreeNode* root) {
        int res = 0;
        greaterSum(root,res);
        return root;
    }
