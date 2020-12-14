//-----------------------------------------------------------------------Acyclic Graph DFS-------------------------------------------
void dfs(vector<vector<int>> &graph, vector<vector<int>> &res,vector<int> temp,int u,int V)
    {
        temp.push_back(u);
        if(u==V-1)
        {
            res.push_back(temp);
            return;
        }
        for(int i=0;i<graph[u].size();i++)
        {
                dfs(graph,res,temp,graph[u][i],V);
        }
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int V = graph.size();
        vector<vector<int>> res;
        vector<int> temp;
        dfs(graph,res,temp,0,V);
        return res;
    }
//-----------------------------------------------------------------------Cyclic Graph DFS-------------------------------------------
void dfs(vector<vector<int>> graph, vector<vector<int>> &res,vector<int> temp,int u,int V,vector<bool> visited)
    {
        visited[u] = true;
        temp.push_back(u);
        if(u==V-1)
        {
            res.push_back(temp);
        }
        for(int i=0;i<graph[u].size();i++)
        {
            if(!visited[graph[u][i]])
            {
                dfs(graph,res,temp,graph[u][i],V,visited);
            }
        }
    }
    
    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        int V = graph.size();
        vector<vector<int>> res;
        vector<int> temp;
        vector<bool> visited(V,false);
        dfs(graph,res,temp,0,V,visited);
        return res;
    }
