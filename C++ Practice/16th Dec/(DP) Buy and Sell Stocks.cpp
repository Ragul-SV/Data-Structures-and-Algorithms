int maxProfit(vector<int>& prices) {
        int min_p = INT_MAX;
        int res = 0;
        int n = prices.size();
        for(int i=0;i<n;i++)
        {
            min_p = min(min_p,prices[i]);
            res = max(res,prices[i]-min_p);
        }
        return res;
    }
