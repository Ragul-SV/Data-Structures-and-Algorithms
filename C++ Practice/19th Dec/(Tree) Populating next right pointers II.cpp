Node* connect(Node* root) {
        Node* head = root;
        Node* temp = new Node(0);
        Node* cur;
        while(root!=NULL)
        {
            cur = temp;
            while(root!=NULL)
            {
                if(root->left!=NULL)
                {
                    cur->next = root->left;
                    cur = cur->next;
                }
                if(root->right!=NULL)
                {
                    cur->next = root->right;
                    cur = cur->next;
                }
                root = root->next;
            }
            root = temp->next;
            temp->next = NULL;
        }
        return head;
    }
