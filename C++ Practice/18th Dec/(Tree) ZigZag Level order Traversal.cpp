vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL)return res;
        map<int,vector<int>> mp;
        map<int,vector<int>>::iterator it;
        queue<pair<TreeNode*,int>> q;
        int level;
        q.push({root,0});
        while(!q.empty())
        {
            level = q.front().second;
            TreeNode* node = q.front().first;
            q.pop();
            mp[level].push_back(node->val);
            if(node->left) q.push({node->left,level+1});
            if(node->right) q.push({node->right,level+1});
        }
        for(it=mp.begin();it!=mp.end();it++)
        {
            if(it->first%2!=0)
            {
                reverse(it->second.begin(),it->second.end());
                res.push_back(it->second);
            }
            else
            {
                res.push_back(it->second);
            }
        }
        return res;
    }
