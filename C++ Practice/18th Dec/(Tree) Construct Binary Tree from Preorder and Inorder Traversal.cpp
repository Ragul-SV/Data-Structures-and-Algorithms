TreeNode* build(vector<int>&preorder, int &preIndex,vector<int> &inorder,int start,int end,map<int,int> &mp)
    {
        if(start>end)return NULL;
        TreeNode* root = new TreeNode(preorder[preIndex++]);
        if(start==end)return root;
        int i = mp[root->val];
        if(i<=end)
        {
            root->left = build(preorder,preIndex,inorder,start,i-1,mp);
            root->right = build(preorder,preIndex,inorder,i+1,end,mp);
        }
        return root;
    }
    
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int preIndex = 0;
        int n = preorder.size();
        map<int,int> mp;
        for(int i=0;i<n;i++)
        {
            mp[inorder[i]] = i;
        }
        return build(preorder,preIndex,inorder,0,n-1,mp);
    }
