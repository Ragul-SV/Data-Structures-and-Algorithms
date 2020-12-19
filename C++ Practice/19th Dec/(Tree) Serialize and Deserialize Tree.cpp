string serialize(TreeNode* root) {
        if(root!=NULL)
            return to_string(root->val)+","+serialize(root->left)+","+serialize(root->right);
        return "#";

    }
    
    int get_element(string &data)
    {
        int pos = data.find(',');
        int val = stoi(data.substr(0,pos));
        data = data.substr(pos+1);
        return val;
    }
    
    TreeNode* deserializeUtil(string &data)
    {
        if(data[0]=='#'){if(data.length()>1)data = data.substr(2);return NULL;}
        TreeNode* root = new TreeNode(get_element(data));
        root->left = deserializeUtil(data);
        root->right = deserializeUtil(data);
        return root;
    }
    
    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        return deserializeUtil(data);
    }
