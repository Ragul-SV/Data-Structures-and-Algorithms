int maxLevelSum(TreeNode* root) {
        if(root==NULL)return 0;
        queue<TreeNode*> q;
        q.push(root);
        int n;
        int maxi = INT_MIN;
        int sum,level=0,res;
        while(!q.empty())
        {
            n = q.size();
            sum = 0;
            level++;
            for(int i=0;i<n;i++)
            {
                TreeNode* node = q.front();
                q.pop();
                sum+=node->val;
                if(node->left)q.push(node->left);
                if(node->right)q.push(node->right);
            }
            if(sum>maxi)
            {
                res = level;
                maxi = sum;
            }
        }
        return res;
    }
