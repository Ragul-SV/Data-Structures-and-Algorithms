vector<int> searchRange(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size()-1;
        int mid;
        vector<int> res(2,-1);
        if(nums.size()==0)return res;
        while(low<high)
        {
            mid = low + (high-low)/2;
            if(nums[mid]<target)
                low = mid+1;
            else
                high = mid;
        }
        if(nums[low]!=target)return res;
        res[0] = low;
        high = nums.size()-1;
        while(low<high)
        {
            mid = low + (high-low)/2 + 1;
            if(nums[mid]>target)
                high = mid-1;
            else
                low = mid;
        }
        if(nums[high]!=target)return res;
        res[1] = high;
        return res;
    }
