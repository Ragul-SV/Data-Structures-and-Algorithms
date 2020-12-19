vector<TreeNode*> generate(int start,int end)
    {
        vector<TreeNode*> res;
        if(start>end)
        {
            res.push_back(NULL);
            return res;
        }
        if(start==end)
        {
            res.push_back(new TreeNode(start));
            return res;
        }
        vector<TreeNode*> l;
        vector<TreeNode*> r;
        for(int i=start;i<=end;i++)
        {
            l = generate(start,i-1);
            r = generate(i+1,end);
            for(TreeNode* nl:l)
            {
                for(TreeNode* nr:r)
                {
                    TreeNode* root = new TreeNode(i);
                    root->left = nl;
                    root->right = nr;
                    res.push_back(root);
                }
            }
        }
        return res;
    }
    
    vector<TreeNode*> generateTrees(int n) {
        if(n==0)return vector<TreeNode*>()={};
        return generate(1,n);
    }
