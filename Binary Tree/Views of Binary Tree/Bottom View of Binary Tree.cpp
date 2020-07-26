void bottom(Node* root,int level,int depth,map<int,pair<int,int>> &mp)
{
    if(root!=NULL)
    {
        if(mp.count(level)==0) mp[level] = make_pair(root->data,depth);
        else if(mp[level].second<=depth) mp[level] = make_pair(root->data,depth);
        bottom(root->left,level-1,depth+1,mp);
        bottom(root->right,level+1,depth+1,mp);
    }
}
// Method that prints the bottom view.
void bottomView(Node *root)
{
   map<int,pair<int,int>> mp;
   map<int,pair<int,int>> ::iterator it;
   bottom(root,0,0,mp);
   for(it=mp.begin();it!=mp.end();it++)
   {
       cout<<(it->second).first<<" ";
   }
}

/*def bottom(root,level,depth,d):
    if root:
        if level not in d:
            d[level] = [root.data,depth]
        elif depth>=d[level][1]:
            d[level] = [root.data,depth]
        bottom(root.left,level-1,depth+1,d)
        bottom(root.right,level+1,depth+1,d)
        
def bottomView(root):
    d = dict()
    bottom(root,0,0,d)
    res = []
    for i in sorted(d):
        res.append(d[i][0])
    return res
    */
