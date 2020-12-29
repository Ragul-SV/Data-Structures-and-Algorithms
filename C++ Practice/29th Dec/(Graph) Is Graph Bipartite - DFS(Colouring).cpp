bool dfs(vector<vector<int>> &graph,vector<int> &color,int c,int u)
    {
        if(color[u]!=0)
            return color[u]==c;
        color[u] = c;
        for(int i=0;i<graph[u].size();i++)
        {
            if(!dfs(graph,color,-c,graph[u][i]))
                return false;
        }
        return true;
    }
    
    bool isBipartite(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> color(n,0);
        for(int i=0;i<n;i++)
        {
            if(color[i]==0 && !dfs(graph,color,1,i))
                return false;
        }
        return true;
    }
