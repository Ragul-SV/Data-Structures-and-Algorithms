vector<vector<int>> verticalTraversal(TreeNode* root) {
        vector<vector<int>> res;
        map<int,vector<int>> mp;
        queue<pair<TreeNode*,int>> q;
        q.push(make_pair(root,0));
        while(!q.empty())
        {
            TreeNode* node = q.front().first;
            int level = q.front().second;
            q.pop();
            mp[level].push_back(node->val);
            if(node->left!=NULL)
            q.push(make_pair(node->left,level-1));
            if(node->right!=NULL)
            q.push(make_pair(node->right,level+1));
        }
        for(auto it=mp.begin();it!=mp.end();it++)
        {
            res.push_back(it->second);
        }
        return res;
    }
