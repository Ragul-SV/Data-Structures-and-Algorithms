int height(Node* root)
{
    if(root==NULL) return 0;
    return 1 + max(height(root->left),height(root->right));
}
    

void printlevel(Node* root,int level,int &sum)
{
    if(root!=NULL)
    {
        if(level==0) sum+=root->data;
        printlevel(root->left,level-1,sum);
        printlevel(root->right,level-1,sum);
    }
}
    
int maxLevelSum(Node *root)
{
    int h = height(root);
    int maxsum = INT_MIN;
    int sum;
    for(int i=0;i<h;i++)
    {
        sum = 0;
        printlevel(root,i,sum);
        if(sum>maxsum)
        {
            maxsum = sum;
        }
    }
    return maxsum;
}
