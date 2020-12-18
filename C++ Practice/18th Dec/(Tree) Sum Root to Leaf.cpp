 void pathsum(TreeNode* root,int path,int &res)
    {
        if(root!=NULL)
        {
            path = path*10+root->val;
            if(root->left==NULL && root->right==NULL)
            {
                res += path;
            }
            pathsum(root->left,path,res);
            pathsum(root->right,path,res);
        }
    }
    
    int sumNumbers(TreeNode* root) {
        int res=0;
        pathsum(root,0,res);
        return res;
    }
