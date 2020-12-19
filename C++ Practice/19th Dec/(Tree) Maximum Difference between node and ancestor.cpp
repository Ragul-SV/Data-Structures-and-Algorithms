void maxdiff(TreeNode* root, int maxi, int mini,int &res)
    {
        if(root==NULL)return;
        res = max(res,max(abs(maxi-root->val),abs(mini-root->val)));
        maxi = max(maxi,root->val);
        mini = min(mini,root->val);
        maxdiff(root->left,maxi,mini,res);
        maxdiff(root->right,maxi,mini,res);
    }
    int maxAncestorDiff(TreeNode* root) {
        int res = 0;
        maxdiff(root,root->val,root->val,res);
        return res;
    }
