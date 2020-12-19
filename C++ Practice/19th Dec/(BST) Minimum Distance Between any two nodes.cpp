void inorder(TreeNode* root,int &p,int &res)
    {
        if(root!=NULL)
        {
            inorder(root->left,p,res);
            if(p!=-1)
            {
                res = min(res,abs(p-root->val));
            }
            p = root->val;
            inorder(root->right,p,res);   
        }
    }
    
    int minDiffInBST(TreeNode* root) {
        int res = INT_MAX;
        int p = -1;
        inorder(root,p,res);
        return res;
    }
