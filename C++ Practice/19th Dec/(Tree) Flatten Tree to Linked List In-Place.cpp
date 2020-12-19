void flat(TreeNode* root, TreeNode* &prev)
    {
        if(root==NULL) return;
        flat(root->right,prev);
        flat(root->left,prev);
        root->right = prev;
        root->left = NULL;
        prev = root;
    }
    
    void flatten(TreeNode* root) {
        TreeNode* prev = NULL;
        flat(root,prev);
    }
