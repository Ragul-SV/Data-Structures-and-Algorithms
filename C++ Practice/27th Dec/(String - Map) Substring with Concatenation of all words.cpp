vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        int n1 = s.length();
        int n2 = words.size();
        int len = words[0].length();
        unordered_map<string,int> word_count;
        for(string w:words)
            word_count[w]++;
        for(int i=0;i<n1-n2*len+1;i++)
        {
            unordered_map<string,int> mp;
            int j=0;
            for(;j<n2;j++)
            {
                string temp = s.substr(i+j*len,len);
                if(word_count.find(temp)!=word_count.end())
                {
                    mp[temp]++;
                    if(mp[temp]>word_count[temp])break;
                }
                else break;
            }
            if(j==n2)res.push_back(i);
        }
        return res;
    }
