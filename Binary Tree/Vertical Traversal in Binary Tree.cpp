void printvertical(Node* root,map<int,vector<int>> &mp, int level)
{
    if(root)
    {
        mp[level].push_back(root->data);
        printvertical(root->left,mp,level-1);
        printvertical(root->right,mp,level+1);
    }
}

// root: root node of the tree
void verticalOrder(Node *root)
{
    map<int,vector<int>> mp;
    map<int,vector<int>> ::iterator it;
    printvertical(root,mp,0);
    for(it=mp.begin();it!=mp.end();it++)
    {
        for (int i=0; i<it->second.size(); i++) 
        cout << it->second[i] << " "; 
    }
}

#---------------------------------------------------Python--------------------------------------------------------#
"""
def printvertical(root,hmap,level):
    if root:
        try:
            hmap[level].append(root.data)
        except:
            hmap[level] = [root.data]
        printvertical(root.left,hmap,level-1)
        printvertical(root.right,hmap,level+1)
        
def verticalOrder(root): 
    hmap = dict()
    printvertical(root,hmap,0)
    for key in sorted(hmap):
        for i in hmap[key]:
            print(i,end=" ")
"""
