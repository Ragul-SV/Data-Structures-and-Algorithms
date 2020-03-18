void inorder(Node* root, vector<Node*>& vec){
    if(root){
      inorder(root->left, vec);
      vec.push_back(root);
      inorder(root->right, vec);
    }
}
Node* balanceBST(vector<Node*>& nodes, int start, int end){
    if(start > end)
        return NULL;
    int mid = (int)(start+end)/2;
    Node *tmp = nodes[mid];
    tmp->left = balanceBST(nodes, start, mid-1);
    tmp->right = balanceBST(nodes, mid+1, end);
    return tmp;
}
Node* buildBalancedTree(Node* root)
{
    vector<Node*> vec;
    inorder(root, vec);
    return balanceBST(vec, 0, vec.size()-1);
}
