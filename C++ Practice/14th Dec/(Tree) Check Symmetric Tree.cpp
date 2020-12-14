bool isSymmetricUtil(TreeNode* a,TreeNode* b)
    {
        if(a==NULL && b==NULL) return true;
        if(a==NULL || b==NULL) return false;
        return a->val==b->val && isSymmetricUtil(a->left,b->right) && isSymmetricUtil(a->right,b->left);
    }
    
    bool isSymmetric(TreeNode* root) {
        return isSymmetricUtil(root,root);   
    }
