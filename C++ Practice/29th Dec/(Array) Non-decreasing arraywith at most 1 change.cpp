bool checkPossibility(vector<int>& nums) {
        bool flag = true;
        int c = -1;
        int n = nums.size();
        for(int i=0;i<n-1;i++)
        {
            if(nums[i]>nums[i+1])
            {
                if(c!=-1)return false;
                c = i;
            }
        }
        return c==-1 || c==0 || c==n-2 || nums[c-1]<=nums[c+1] || nums[c]<=nums[c+2];
    }
