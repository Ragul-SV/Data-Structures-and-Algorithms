bool isEvenOddTree(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        while(!q.empty())
        {
            int temp=-1;
            int n = q.size();
            for(int i=0;i<n;i++)
            {
                TreeNode* root = q.front();
                q.pop();
                if(level%2==0 && (root->val%2==0 || (temp!=-1 &&temp>=root->val))){return false;}
                else if(level%2!=0 && (root->val%2!=0 || (temp!=-1 && temp<=root->val))){return false;}
                temp = root->val;
                if(root->left!=NULL)q.push(root->left);
                if(root->right!=NULL)q.push(root->right);
            }
            level++;
            }
        return true;
        }
