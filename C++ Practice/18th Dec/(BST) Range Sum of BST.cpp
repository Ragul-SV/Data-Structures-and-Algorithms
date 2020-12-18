void range(TreeNode* root, int &low, int &high,int &res)
    {
        if(root!=NULL)
        {
            if(root->val>=low && root->val<=high)
                res+=root->val;
            if(root->val>low)
                range(root->left,low,high,res);
            if(root->val<high)
                range(root->right,low,high,res);
        }
    }
    
    int rangeSumBST(TreeNode* root, int low, int high) {
        int res = 0;
        range(root,low,high,res);
        return res;
    }
