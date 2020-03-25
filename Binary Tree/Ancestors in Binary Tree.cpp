#include<string>  
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
// Function should print all the ancestor of the target node
bool printAncestors(struct Node *root, int target)
{
     vector<int> vec;
     ancestors(root,target,vec);
}
