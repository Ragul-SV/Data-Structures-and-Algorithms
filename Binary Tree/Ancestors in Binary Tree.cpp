//-----------------------------------------------------METHOD 1--------------------------------------------------------------//
void ancestors(struct Node* root,int target,vector<int> vec)
{
    if(root!=NULL)
    {   
        if(root->data==target)
        {
            for(int i=vec.size()-1;i>=0;i--)
            {
                cout<<vec[i]<<" ";
            }
        }
        else
        {
            vec.push_back(root->data); 
            ancestors(root->left,target,vec);
            ancestors(root->right,target,vec);
        }
    }
}

bool printAncestors(struct Node *root, int target)
{
     vector<int> vec;
     ancestors(root,target,vec);
}

//----------------------------------------------------METHOD 2-----------------------------------------------------------------//
bool printAncestors(struct Node *root, int target)
{
    if(root==NULL) return false;
    if(root->data==target) return true;
    if(printAncestors(root->left,target) || printAncestors(root->right,target))
    {
        cout<<root->data<<" ";
        return true;
    }
}
