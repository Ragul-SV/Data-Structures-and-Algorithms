vector<string> commonChars(vector<string>& A) {
        vector<int> count(26,INT_MAX);
        vector<string> res;
        for(int i=0;i<A.size();i++)
        {
            vector<int> temp(26,0);
            for(int j=0;j<A[i].length();j++)
            {
                temp[A[i][j]-'a']++;
            }
            for(int i=0;i<26;i++)
            {
                count[i] = min(count[i],temp[i]);
            }
        }
        for(int i=0;i<26;i++)
        {
            for(int j=0;j<count[i];j++)
            {
                string s;                   //string to char only works separately
                s = (char) i+(int)'a';
                res.push_back(s);
            }
        }
        return res;
    }
