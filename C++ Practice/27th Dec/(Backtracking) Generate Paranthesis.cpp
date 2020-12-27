void backtrack(int n,string s,int open,int close, vector<string> &res)
    {
        if(s.length()==n*2){res.push_back(s);return;}
        if(open<n)
            backtrack(n,s+"(",open+1,close,res);
        if(close<open)
            backtrack(n,s+")",open,close+1,res);
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        backtrack(n,"",0,0,res);
        return res;
    }
