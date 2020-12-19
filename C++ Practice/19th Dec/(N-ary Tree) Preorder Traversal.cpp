void pre(Node* root,vector<int> &res)
    {
        if(root!=NULL)
        {
            res.push_back(root->val);
            for(Node* node:root->children)
            {
                pre(node,res);
            }
        }
    }
    
    vector<int> preorder(Node* root) {
        vector<int> res;
        pre(root,res);
        return res;
    }
