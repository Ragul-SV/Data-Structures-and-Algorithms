int maxSubArray(vector<int>& nums) {
        int cur_max=INT_MIN,max_ending=0; 
        for(int i=0;i<nums.size();i++)
        {
            max_ending = max_ending+nums[i];
            cur_max = max(cur_max,max_ending);
            if(max_ending<0)max_ending = 0;
        }
        return cur_max;
    }
