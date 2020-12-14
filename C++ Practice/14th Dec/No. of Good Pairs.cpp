//------------------------------------------METHOD1------------------------------
int numIdenticalPairs(vector<int>& nums) {
        map<int,vector<int>> mp;
        map<int,vector<int>>:: iterator it;
        int res = 0;
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]].push_back(i);
        }
        for(it=mp.begin();it!=mp.end();it++)
        {
            res+=((it->second.size())*(it->second.size()-1))/2;
        }
        return res;
    }
//------------------------------------------METHOD2------------------------------
int numIdenticalPairs(vector<int>& nums) {
        map<int,int> mp;
        int res = 0;
        for(int i=0;i<nums.size();i++)
        {
            res+=(mp[nums[i]]++);
        }
        return res;
    }    
