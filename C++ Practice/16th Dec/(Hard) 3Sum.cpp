vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(),nums.end());
        int n = nums.size();
        int target,front,rear,sum;
        for(int i=0;i<n;i++)
        {
            target = -nums[i];
            front = i+1;
            rear = n-1;
            while(front<rear)
            {
                sum = nums[front]+nums[rear];
                if(sum<target)front++;
                else if(sum>target)rear--;
                else
                {
                    vector<int>temp(3,0);
                    temp[0] = nums[i];
                    temp[1] = nums[front];
                    temp[2] = nums[rear];
                    res.push_back(temp);
                    while(front<rear && nums[front]==temp[1])front++;
                    while(front<rear && nums[rear]==temp[2])rear--;
                }
            }
            while(i+1<n && nums[i]==nums[i+1])i++;
        }
        return res;
    }
