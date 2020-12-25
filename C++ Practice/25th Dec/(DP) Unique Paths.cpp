//---------------------------------------------O(N^2) Space Complexity------------------------------------
int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m,vector<int>(n,0));
        for(int i=0;i<m;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(i==0 || j==0) dp[i][j] = 1;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
//---------------------------------------------O(N) Space Complexity------------------------------------
int uniquePaths(int m, int n) {
        int dp[n];
        fill(dp,dp+n,1);
        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                dp[j] += dp[j-1];
            }
        }
        return dp[n-1];
    }
