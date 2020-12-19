Node* connect(Node* root) {
        if(root==NULL)return NULL;
        Node* prev = root;
        Node* cur = NULL;
        while(prev->left!=NULL)
        {
            cur = prev;
            while(cur!=NULL)
            {
                cur->left->next = cur->right;
                if(cur->next) cur->right->next = cur->next->left;
                cur = cur->next;
            }
            prev = prev->left;
        }
        return root;
    }
