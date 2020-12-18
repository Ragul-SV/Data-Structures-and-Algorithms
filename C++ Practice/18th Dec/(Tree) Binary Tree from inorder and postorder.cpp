TreeNode* build(vector<int> &inorder, vector<int>& postorder,int &postIndex,int start,int end,map<int,int> &mp)
    {
        if(start>end)return NULL;
        TreeNode* root = new TreeNode(postorder[postIndex--]);
        int i = mp[root->val];
        root->right = build(inorder,postorder,postIndex,i+1,end,mp);
        root->left = build(inorder,postorder,postIndex,start,i-1,mp);
        return root;
    }
    
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        int n = inorder.size();
        int postIndex = n-1;
        map<int,int> mp;
        for(int i=0;i<n;i++)
        {
            mp[inorder[i]] = i;
        }
        return build(inorder,postorder,postIndex,0,n-1,mp);
    }
