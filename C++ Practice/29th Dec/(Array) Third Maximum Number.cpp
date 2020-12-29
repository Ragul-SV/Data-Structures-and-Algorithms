int thirdMax(vector<int>& nums) {
        int64_t maxA,maxB,maxC;
        maxA = maxB = maxC = -2147483648-1;
        int n = nums.size();
        for(int i=0;i<n;i++)
        {
            if(nums[i]>=maxA)
            {
                if(nums[i]!=maxA)
                {
                    maxC = maxB;
                    maxB = maxA;
                    maxA = nums[i];
                }     
            }
            else if(nums[i]>=maxB)
            {
                if(nums[i]!=maxB)
                {
                    maxC = maxB;
                    maxB = nums[i];
                }     
            }
            else if(nums[i]>=maxC)
            {
                maxC = nums[i];
            }
        }
        if(maxC==-2147483648-1)return maxA;
        return maxC;
        
    }
