Node *convertToDLL(Node *root, Node **head_ref)
{
    if(root == NULL)return NULL;
    static Node *prev = NULL;
    if(root->left==NULL && root->right == NULL)
    {
        if(*head_ref==NULL)
        {
            prev=root;
            *head_ref = root;
        }
        else
        {
            prev->right = root;
            root->left = prev;
            prev = root;
        }
        return NULL;
    }
    root->left = convertToDLL(root->left,&(*head_ref));
    root->right = convertToDLL(root->right,&(*head_ref));
    return root;
}
