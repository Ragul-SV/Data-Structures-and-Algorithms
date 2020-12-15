void inorder(TreeNode* root,vector<TreeNode*> &in)
    {
        if(root!=NULL)
        {
            inorder(root->left,in);
            in.push_back(root);
            inorder(root->right,in);
        }
    }
    
    TreeNode* balance(vector<TreeNode*> &in,int start,int end)
    {
        if(start>end) return NULL;
        int mid = (start+end)/2;
        TreeNode* node = in[mid];
        node->left = balance(in,start,mid-1);
        node->right = balance(in,mid+1,end);
        return node;
    }
    
    TreeNode* balanceBST(TreeNode* root) {
        vector<TreeNode*> in;
        inorder(root,in);
        return balance(in,0,in.size()-1);
    }
