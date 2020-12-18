bool find(TreeNode* root,int k,unordered_set<int> &s)
    {
        
        if(root==NULL) return false;
        if(s.count(k - root->val)) return true;
        s.insert(root->val);
        return find(root->left,k,s) || find(root->right,k,s);
    }
    
    bool findTarget(TreeNode* root, int k) {
        unordered_set<int> s;
        return find(root,k,s);
    }
