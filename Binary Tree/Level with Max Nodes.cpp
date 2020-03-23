int height(Node* root)
{
    if(root==NULL) return 0;
    return 1 + max(height(root->left),height(root->right));
}
    

void printlevel(Node* root,int level,int &count)
{
    if(root!=NULL)
    {
        if(level==0) count+=1;
        printlevel(root->left,level-1,count);
        printlevel(root->right,level-1,count);
    }
}
    
int maxNodeLevel(Node *root)
{
    int h = height(root);
    int maxlevel = 0;
    int maxnum = 0;
    int count;
    for(int i=0;i<=h;i++)
    {
        count = 0;
        printlevel(root,i,count);
        if(count>maxnum)
        {
            maxnum = count;
            maxlevel = i;
        }
    }
    return maxlevel;
}
