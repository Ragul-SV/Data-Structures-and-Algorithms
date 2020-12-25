int uniquePathsWithObstacles(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        if(grid[0][0]==1)return 0;
        for(int i = 0;i<m;i++)
        {
            if(grid[i][0]==1)
            {
                grid[i][0]=0;
                while(i<m)
                {
                    if(grid[i][0]==1)grid[i][0] = 0;
                    i++;
                }
                break;
            }
            grid[i][0] = 1;
        }
         
        for(int j = 1;j<n;j++)
        {
            if(grid[0][j]==1)
            {
                grid[0][j]=0;
                while(j<n)
                {
                    if(grid[0][j]==1)grid[0][j] = 0;
                    j++;
                }
                break;
            }
            grid[0][j] = 1;
        }
       
        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                if(grid[i][j]==1)grid[i][j] = 0;
                else
                    grid[i][j] = grid[i-1][j] + grid[i][j-1];
            }
        }
        
        return grid[m-1][n-1];
    }
