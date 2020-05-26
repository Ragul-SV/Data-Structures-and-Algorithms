void vertical(Node* root, int level, map<int,int> &mp)
{
    if(root==NULL) return;
    mp[level]+=root->data;
    vertical(root->left,level-1,mp);
    vertical(root->right,level+1,mp);
}

void verticalSum(Node *root) {
    map<int,int> mp;
    map<int,int> ::iterator it;
    vertical(root,0,mp);
    for(it=mp.begin();it!=mp.end();it++) cout<<it->second<<" ";
}

#--------------------------------------------Using Python Dictionaries---------------------------------------#

def vertical(root,level,hmap):
    if not root:
        return 
    try:
        hmap[level]+=root.data
    except KeyError:
        hmap[level]=root.data
    vertical(root.left,level-1,hmap)
    vertical(root.right,level+1,hmap)
    
def verticalSum(root):
    if not root:
        return
    hmap = dict()
    vertical(root,0,hmap)      
    arr = list(hmap.keys())
    arr.sort()
    for key in arr:
        print(hmap[key],end=" ")
