void addRow(TreeNode* root,int &v,int &d,int cur)
    {
        if(root==NULL)return;
        if(cur==d-1)
        {
            TreeNode* node = root->left;
            root->left = new TreeNode(v);
            root->left->left = node;
            node = root->right;
            root->right = new TreeNode(v);
            root->right->right = node;
        }
        else
        {
            addRow(root->left,v,d,cur+1);
            addRow(root->right,v,d,cur+1);
        }
    }
    
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if(d==1)
        {
            TreeNode* node = new TreeNode(v);
            node->left = root;
            return node;
        }
        addRow(root,v,d,1);
        return root;
    }
