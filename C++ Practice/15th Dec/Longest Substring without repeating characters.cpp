//-------------------------------------------Sliding Window-----------------------------------
int lengthOfLongestSubstring(string s) {
        set<char> st;
        int res = 0,len = s.length();
        int i=0,j=0;
        while(i<len && j<len)
        {
            if(st.find(s[j])==st.end())
            {
                st.insert(s[j]);
                j++;
                res = max(res,j-i);
            }
            else
            {
                st.erase(s[i]);
                i++;
            }
        }
        return res;
    }
    //-------------------------------------------Optimized Sliding Window-----------------------------------
    int lengthOfLongestSubstring(string s) {
        vector<int> vec(256,0);
        int res = 0,len = s.length();
        int i=0;
        for(int j=0;j<len;j++)
        {
            if(vec[s[j]]>0)
                i = max(i,vec[s[j]]);
            res = max(res,j-i+1);
            vec[s[j]] = j+1;
        }
        return res;
    }
