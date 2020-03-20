int height(Node* root)
{
    if(root==NULL)
        return 0;
    return root->height;
}

int get_balance(Node* root)
{
    if(root==NULL) 
        return 0;
    return (height(root->left) - height(root->right));
}

Node* left_rotate(Node* z)
{
    Node* y = z->right;
    Node* temp = y->left;
    
    y->left = z;
    z->right = temp;
    
    z->height = 1+max(height(z->left),height(z->right));
    y->height = 1+max(height(y->left),height(y->right));
    
    return y;
}

Node* right_rotate(Node* z)
{
    Node* y = z->left;
    Node* temp = y->right;
    
    y->right = z;
    z->left= temp;
    
    z->height = 1+max(height(z->left),height(z->right));
    y->height = 1+max(height(y->left),height(y->right));
    
    return y;
}
/*You are required to complete this method */

Node* insertToAVL( Node* root, int data)
{
    if(root==NULL)
    {
        Node* node = new Node(data);
        return node;
    }
    
    if(data<root->data)
        root->left=insertToAVL(root->left,data);
    else if(data>root->data)
        root->right=insertToAVL(root->right,data);
    
    root->height = 1+max(height(root->left),height(root->right));
    int balance = get_balance(root);
    
    if(balance>1 && data<root->left->data)
    {
        return right_rotate(root);
    }
    if(balance>1 && data>root->left->data)
    {
        root->left = left_rotate(root->left);
        return right_rotate(root);
    }
    if(balance<-1 && data>root->right->data)
    {
        return left_rotate(root);
    }
    if(balance<-1 && data<root->right->data)
    {
        root->right = right_rotate(root->right);
        return left_rotate(root);
    }
    return root;
}
