TreeNode* construct(vector<int>& preorder,int &preIndex,int mini,int maxi,int &n)
    {
        if(preIndex>=n)return NULL;
        TreeNode* root = NULL;
        if(preorder[preIndex]>mini && preorder[preIndex]<maxi)
        {
            root= new TreeNode(preorder[preIndex++]);
            if(preIndex<n)
            {
                root->left = construct(preorder,preIndex,mini,root->val,n);
                root->right = construct(preorder,preIndex,root->val,maxi,n);
            }
        }
        return root;
    }
    
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        int n = preorder.size();
        int preIndex = 0;
        return construct(preorder,preIndex,INT_MIN,INT_MAX,n);
    }
