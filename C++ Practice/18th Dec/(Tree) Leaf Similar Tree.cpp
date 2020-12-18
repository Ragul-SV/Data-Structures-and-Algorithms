void preorder(TreeNode* root,vector<int> & vec)
    {
        if(root!=NULL)
        {
            if(root->left==NULL && root->right==NULL)
                vec.push_back(root->val);
            preorder(root->left,vec);
            preorder(root->right,vec);
        }
    }
    
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> vec1;
        preorder(root1,vec1);
        vector<int> vec2;
        preorder(root2,vec2);
        return vec1==vec2;
    }
