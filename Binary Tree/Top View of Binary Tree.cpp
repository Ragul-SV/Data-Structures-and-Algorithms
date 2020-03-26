void printTopView(Node* root,int level,int depth,map<int,pair<int,int>> &mp)
{
    if(root)
    {
        if(mp.count(level)==0) 
            mp[level] = make_pair(root->data,depth);
        else if(mp[level].second>depth) 
            mp[level] = make_pair(root->data,depth);
        printTopView(root->left,level-1,depth+1,mp);
        printTopView(root->right,level+1,depth+1,mp);
    }
}

// function should print the topView of the binary tree
void topView(struct Node *root)
{
    map<int,pair<int,int>> mp;
    map<int,pair<int,int>> ::iterator it;
    printTopView(root,0,0,mp);
    for(it=mp.begin();it!=mp.end();it++) cout<<(it->second).first<<" ";
}
