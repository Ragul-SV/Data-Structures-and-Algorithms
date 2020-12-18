void right(TreeNode* root,int level,vector<int> &res)
    {
        if(root!=NULL)
        {
            if(level>res.size()) res.push_back(root->val);
            right(root->right,level+1,res);
            right(root->left,level+1,res);
        }
    }
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        right(root,1,res);
        return res;
    }
