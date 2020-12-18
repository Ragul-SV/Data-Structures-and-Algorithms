vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if(root==NULL)return res;
        queue<TreeNode*> q;
        q.push(root);
        vector<int> temp;
        while(!q.empty())
        {
            int n = q.size();
            temp.clear();
            for(int i=0;i<n;i++)
            {
                TreeNode* node = q.front();
                q.pop();
                temp.push_back(node->val);
                if(node->left!=NULL) q.push(node->left);
                if(node->right!=NULL) q.push(node->right);
            }
            res.insert(res.begin(),temp);
        }
        return res;
        
        
    }
