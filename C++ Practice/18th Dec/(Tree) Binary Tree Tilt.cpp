int tilt(TreeNode* root,int &res)
    {
        if(root==NULL)return 0;
        int l = tilt(root->left,res);
        int r = tilt(root->right,res);
        res+=abs(l-r);
        return l + r + root->val;
    }
    int findTilt(TreeNode* root) {
        int res = 0;
        tilt(root,res);
        return res;
    }
