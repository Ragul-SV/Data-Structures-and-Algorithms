void findPreSuc(Node* root, Node*& pre, Node*& suc, int key)
{
// Your code goes here
    while(root!=NULL)
    {
        if(root->key == key)
        {
            if(root->right)
            {
                Node* temp = root->right;
                while(temp->left)
                {
                    temp = temp->left;
                }
                suc = temp;
            }
            if(root->left)
            {
                Node* temp = root->left;
                while(temp->right)
                {
                    temp = temp->right;
                }
                pre = temp;
            }
            break;
        }
        else if(key < root->key)
        {
            suc = root;
            root = root->left;
        }
        else
        {
            pre = root;
            root = root->right;
        }
    }
}
