static bool cmp(pair<char,int>& a, pair<char,int>& b)
    {
        return a.second>b.second;
    }
    
    string frequencySort(string s) {
        unordered_map<char,int> mp;
        unordered_map<char,int>::iterator it;
        for(int i=0;i<s.length();i++)
        {
            mp[s[i]]++;
        }
        vector<pair<char,int>> vec;
        for(it=mp.begin();it!=mp.end();it++)
        {
            vec.push_back(make_pair(it->first,it->second));
        }
        sort(vec.begin(),vec.end(),cmp);
        string res;
        for(int i=0;i<vec.size();i++)
        {
            while(vec[i].second--)res+=vec[i].first;
        }
        return res;
    }
