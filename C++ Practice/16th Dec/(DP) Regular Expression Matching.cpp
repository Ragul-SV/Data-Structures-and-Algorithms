bool isMatch(string s, string p) {
        if(p.empty())
            return s.empty();
        bool match = (s.length()!=0) && (p[0]==s[0] || p[0]=='.');
        
        if(p.length()>=2 && p[1]=='*')
        {
            return (isMatch(s,p.substr(2)) || match && isMatch(s.substr(1),p));
        }
        else
        {
            return match &&  isMatch(s.substr(1),p.substr(1));
        }
}

//--------------------------------------------(DP)---Top Down------Optimized---------------------------
bool check(string s,string p,int i,int j,map<pair<int,int>,bool> &mp)
    {
        bool res;
        if(mp.find(make_pair(i,j))==mp.end())
        {
            if(j==p.length())
                res = i==s.length();
            else
            {
                bool match = i<s.length() && (p[j]==s[i] || p[j]=='.');
                if(j+1<p.length() && p[j+1]=='*')
                {
                    res = check(s,p,i,j+2,mp) || match && check(s,p,i+1,j,mp);
                }
                else
                {
                    res = match && check(s,p,i+1,j+1,mp);
                }
            }
            mp[make_pair(i,j)] = res;
        }
        return mp[make_pair(i,j)];
    }
    
    bool isMatch(string s, string p) {
        map<pair<int,int>,bool> mp;
        return check(s,p,0,0,mp);
    }
//--------------------------------------------(DP)---Bottom Up------Optimized---------------------------
int lens=s.length(),lenp=p.length();
    vector<vector<bool>> dp(lens+1,vector<bool>(lenp+1,false));
    dp[lens][lenp] = true;
    for(int i=lens;i>=0;i--)
    {
        for(int j=lenp-1;j>=0;j--)
        {
            bool match = i<lens && (p[j]==s[i] || p[j]=='.');
            if(j+1<lenp && p[j+1]=='*')
            {
                dp[i][j] = dp[i][j+2] || (match && dp[i+1][j]);
            }
            else
                dp[i][j] = match && dp[i+1][j+1];
        }
    }
    return dp[0][0];
    }
