void path(TreeNode* root, vector<int> &p,int s,int &sum,vector<vector<int>> &res)
    {
        if(root!=NULL)
        {
            s+=root->val;
            p.push_back(root->val);
            if(root->left==NULL && root->right==NULL)
            {
                if(s==sum)
                {
                    res.push_back(p);
                }
            }
            path(root->left,p,s,sum,res);
            path(root->right,p,s,sum,res);
            p.pop_back();
        }
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> p;
        path(root,p,0,sum,res);
        return res;
    }
