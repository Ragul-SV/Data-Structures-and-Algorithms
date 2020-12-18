TreeNode* construct(vector<int> &nums,int start,int end)
    {
        if(start<=end)
        {
            int mid = (start+end)/2;
            TreeNode* root = new TreeNode(nums[mid]);
            root->left = construct(nums,start,mid-1);
            root->right = construct(nums,mid+1,end);
            return root;
        }
        return NULL;
    }
    
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return construct(nums,0,nums.size()-1);
    }
