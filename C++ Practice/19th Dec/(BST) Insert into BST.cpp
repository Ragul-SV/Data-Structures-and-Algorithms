TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(root==NULL)return new TreeNode(val);
        TreeNode* h = root;
        while(root!=NULL)
        {
            if(val>root->val){
                if(root->right==NULL)
                {root->right=new TreeNode(val);break;}
                root = root->right;
            }
            if(val<root->val){
                if(root->left==NULL)
                {root->left=new TreeNode(val);break;}
                root = root->left;
            }
        }
        return h;
    }
