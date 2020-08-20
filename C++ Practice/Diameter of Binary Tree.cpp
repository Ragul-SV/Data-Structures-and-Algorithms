int find_diameter(Node* node,int *height)
{
    int lh = 0,rh = 0;
    if(node==NULL)
    {
        *height = 0;
        return 0;
    }
    int ldiameter = find_diameter(node->left,&lh);
    int rdiameter = find_diameter(node->right,&rh);
    *height = 1+max(lh,rh);
    return max(1+lh+rh,max(ldiameter,rdiameter));
}

/* Computes the diameter of binary tree with given root.  */
int diameter(Node* node) {
    int height = 0;
    return find_diameter(node,&height);
}
