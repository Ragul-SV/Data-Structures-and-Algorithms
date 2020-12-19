vector<int> pathInZigZagTree(int label) {
        int level = 0;
        vector<int> res;
        while(1<<level <= label) level++;
        while(label>=1)
        {
            res.insert(res.begin(),label);
            label = (1<<level)-1 + (1<<(level-1)) - label;
            label/=2;
            level-=1;
        }
        return res;
    }
