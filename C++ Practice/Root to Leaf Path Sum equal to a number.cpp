bool hasPathSum(Node *node, int sum) {
    if(node==NULL)return (sum==0);
    if(node->left==NULL && node->right==NULL && sum-node->data==0)return true;
    return hasPathSum(node->left,sum-node->data) or hasPathSum(node->right,sum-node->data);
}
