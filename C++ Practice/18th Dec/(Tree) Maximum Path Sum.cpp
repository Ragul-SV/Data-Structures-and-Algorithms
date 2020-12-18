int maxPathSum(TreeNode* root) {
        int res = INT_MIN;
        maxPath(root,res);
        return res;
    }
    int maxPath(TreeNode* root,int &res)
    {
        if(root==NULL)return 0;
        int l = max(0,maxPath(root->left,res));
        int r = max(0,maxPath(root->right,res));
        res = max(res,root->val+l+r);
        return max(l,r)+root->val;
    }
