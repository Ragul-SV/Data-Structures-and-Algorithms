void dfs(vector<vector<int>> &vec,int n,int i,int j)
    {
        if(i>=0 && j>=0 && i<3*n && j<3*n && vec[i][j]==0)
        {
            vec[i][j]=1;
            dfs(vec,n,i-1,j),dfs(vec,n,i+1,j),dfs(vec,n,i,j-1),dfs(vec,n,i,j+1);
        }
    }
    
    int regionsBySlashes(vector<string>& grid) {
        int n = grid.size();
        vector<vector<int>> vec(n*3,vector<int>(n*3,0));
        int res=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<n;j++)
            {
                if(grid[i][j]=='/')
                {
                    vec[i*3][j*3+2]=vec[i*3+1][j*3+1]=vec[i*3+2][j*3]=1; 
                }
                if(grid[i][j]=='\\')
                {
                    vec[i*3][j*3]=vec[i*3+1][j*3+1]=vec[i*3+2][j*3+2]=1; 
                }
            }
        }
        
        for(int i=0;i<n*3;i++)
        {
            for(int j=0;j<n*3;j++)
            {
                if(vec[i][j]==0){dfs(vec,n,i,j);res++;}
            }
        }
        return res;
    }
