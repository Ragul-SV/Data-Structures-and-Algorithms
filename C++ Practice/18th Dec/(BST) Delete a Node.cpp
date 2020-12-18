TreeNode* deleteNode(TreeNode* root, int key) {
        if(root==NULL) return NULL;
        if(root->val>key)
        {
            root->left = deleteNode(root->left,key);
            return root;
        }
        else if(root->val<key){
            root->right = deleteNode(root->right,key);
            return root;
        }
        if(root->left==NULL)
        {
            TreeNode* temp = root->right;
            delete root;
            return temp;
        }
        else if(root->right==NULL)
        {
            TreeNode* temp = root->left;
            delete root;
            return temp;
        }
        else
        {
            TreeNode* par_succ = root;
            TreeNode* succ = root->right;
            while(succ!=NULL && succ->left!=NULL)
            {
                par_succ = succ;
                succ = succ->left;
            }
            root->val = succ->val;
            if(par_succ==root)
                par_succ->right = succ->right;
            else
                par_succ->left = succ->right;
            
            delete succ;
            return root;
        }
    }
