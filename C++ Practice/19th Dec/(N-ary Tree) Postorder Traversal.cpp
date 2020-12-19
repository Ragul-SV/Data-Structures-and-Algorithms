void post(Node* root,vector<int> &res)
    {
        if(root!=NULL)
        {
            for(Node* node:root->children)
            {
                post(node,res);
            }
            res.push_back(root->val);
        }
    }
    
    vector<int> postorder(Node* root) {
        vector<int> res;
        post(root,res);
        return res;
    }
