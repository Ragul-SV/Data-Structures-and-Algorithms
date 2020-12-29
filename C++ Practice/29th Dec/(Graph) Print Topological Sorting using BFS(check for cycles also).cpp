vector<int> findOrder(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> g(n);
        vector<int> degree(n,0);
        queue<int> q;
        vector<int> order;
        for(vector<int> pre:prerequisites)
        {
            g[pre[1]].push_back(pre[0]);
            degree[pre[0]]++;
        }
        for(int i=0;i<n;i++)
        {
            if(degree[i]==0)
                q.push(i);
        }
        int count = n;
        while(!q.empty())
        {
            int course = q.front();
            q.pop();
            count--;
            order.push_back(course);
            for(int i=0;i<g[course].size();i++)
            {
                if(--degree[g[course][i]]==0)
                    q.push(g[course][i]);
            }
        }
        if(count!=0)
            return vector<int>();
        return order;
    }
