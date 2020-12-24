#------------------------------------------O(N)-TIME------O(N)-SPACE-------------------#
int longestValidParentheses(string s) {
        int n = s.length();
        vector<int> dp(n,0);
        int res = 0;
        for(int i=1;i<n;i++)
        {
            if(s[i]==')')
            {
                if(s[i-1]=='(')
                    dp[i] = (i-2>=0?dp[i-2]:0) + 2;
                else if(i-dp[i-1]-1>=0 && s[i-dp[i-1]-1]=='(')
                    dp[i] = dp[i-1] + (i-dp[i-1]-2>=0?dp[i-dp[i-1]-2]:0) + 2;
                res = max(res,dp[i]);
            }
        }
        return res;
    }

#------------------------------------------O(N)-TIME------O(1)-SPACE-------------------#
int longestValidParentheses(string s) {
        int n = s.length();
        int res = 0;
        int left=0,right=0;
        for(int i=0;i<n;i++)
        {
            if(s[i]=='(')left++;
            else right++;
            if(left==right)res = max(res,left*2);
            else if(right>left)left = right = 0;
        }
        left = right = 0;
        for(int i=n-1;i>=0;i--)
        {
            if(s[i]=='(')left++;
            else if(s[i]==')')right++;
            if(left==right)res = max(res,left*2);
            else if(left>right)left = right = 0;
        }
        return res;
    }
