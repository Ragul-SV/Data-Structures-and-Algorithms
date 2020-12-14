void dfs(vector<vector<int>>& rooms,int u,int n,vector<bool> &visited)
    {
        visited[u] = true;
        for(int i=0;i<rooms[u].size();i++)
        {
            if(visited[rooms[u][i]]==false)
            {
                dfs(rooms,rooms[u][i],n,visited);
            }
        }
    }
    
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        int count=1;
        vector<bool> visited(n,false);
        dfs(rooms,0,n,visited);
        for(int i=0;i<n;i++)
        {
            if(visited[i]==false)return false;
        }
        return true;
    }
