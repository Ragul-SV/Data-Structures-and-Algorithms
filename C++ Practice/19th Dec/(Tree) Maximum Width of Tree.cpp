unsigned long int dfs(TreeNode* root,int level,unsigned long int order,vector<pair<unsigned long int,unsigned long int>> & vec)
    {
        if(root==NULL)return 0;
        if(vec.size()==level)vec.push_back({order,order});
        else vec[level].second = order;
        return max({vec[level].second - vec[level].first + 1, dfs(root->left,level+1,2*order,vec),dfs(root->right,level+1,2*order+1,vec)});
    }

    int widthOfBinaryTree(TreeNode* root) {
        vector<pair<unsigned long int,unsigned long int>> vec;
        return dfs(root,0,1,vec);
    }
