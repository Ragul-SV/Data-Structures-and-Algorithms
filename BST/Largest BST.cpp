struct Info 
{ 
    int size;
    int min; 
    int max; 
    int ans; 
    bool isBST; 
}; 
  

Info largest(Node* root) 
{ 
    if (root == NULL) 
        return {0, INT_MAX, INT_MIN, 0, true}; 
    if (root->left == NULL && root->right == NULL) 
        return {1, root->data, root->data, 1, true}; 

    Info l = largest(root->left); 
    Info r = largest(root->right); 

    Info temp; 
    temp.size = (1 + l.size + r.size); 
    temp.min = min(l.min, min(root->data,r.min)); 
    temp.max = max(r.max, max(root->data,l.max));
    if (l.isBST && r.isBST && l.max < root->data && 
            r.min > root->data) 
    { 
        temp.ans = temp.size; 
        temp.isBST = true; 
        return temp; 
    } 
  
    temp.ans = max(l.ans, r.ans); 
    temp.isBST = false;
    return temp; 
} 
int largestBst(Node *root)
{
	return largest(root).ans;
}
