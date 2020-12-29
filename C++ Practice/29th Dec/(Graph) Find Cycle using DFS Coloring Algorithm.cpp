bool cycle(vector<vector<int>> &G,vector<int> &visited, int u)
    {
        if(visited[u]==1)
            return true;
        if(visited[u]==0)
        {
            visited[u] = 1;
            for(int i=0;i<G[u].size();i++)
            {
                if(cycle(G,visited,G[u][i]))
                    return true;
            }
        }
        visited[u] = 2;
        return false;
    }
    
    bool canFinish(int n, vector<vector<int>>& prerequisites) {
        vector<vector<int>> G(n);
        for(vector<int> pre:prerequisites)
        {
            G[pre[1]].push_back(pre[0]);
        }
        vector<int> visited(n,0);
        for(int i=0;i<n;i++)
        {
            if(cycle(G,visited,i))
                return false;
        }
        return true;
    }
