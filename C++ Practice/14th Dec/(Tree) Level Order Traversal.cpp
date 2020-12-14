int height(TreeNode* root)
    {
        if(root==NULL)return 0;
        return 1+max(height(root->left),height(root->right));
    }
    
    vector<vector<int>> levelOrder(TreeNode* root) {
        int h = height(root);
        vector<vector<int>> res(h);
        if(root!=NULL)
        {
        queue<pair<TreeNode*,int>> q;
        q.push(make_pair(root,0));
        int l;
        while(!q.empty())
        {
            TreeNode* cur = q.front().first;
            l = q.front().second;
            q.pop();
            res[l].push_back(cur->val);
            if(cur->left!=NULL)
            q.push(make_pair(cur->left,l+1));
            if(cur->right!=NULL)
            q.push(make_pair(cur->right,l+1));
        }
        }
        return res;
    }
