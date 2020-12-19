int maxDepth(Node* root) {
        if(root==NULL)return 0;
        int maxd = 0;
        for(int i=0;i<root->children.size();i++)
        {
            maxd = max(maxd,maxDepth(root->children[i]));
        }
        return 1+maxd;
    }
