vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int> res, visited(n);
        for(int i=0;i<edges.size();i++)
        {
            visited[edges[i][1]] = 1;
        }
        for(int i=0;i<n;i++)
        {
            if(visited[i]==0)res.push_back(i);
        }
        return res;
    }
