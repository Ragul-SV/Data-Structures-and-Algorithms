int minDistance(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        vector<vector<int>> dp(n1+1,vector<int>(n2+1));
        for(int i=0;i<=n1;i++)
        {
            for(int j=0;j<=n2;j++)
            {
                if(i==0)dp[i][j] = j;
                else if(j==0)dp[i][j] = i;
                else if(word1[i-1]==word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else dp[i][j] = min(dp[i-1][j],min(dp[i-1][j-1],dp[i][j-1])) + 1;
            }
        }
        return dp[n1][n2];
    }
