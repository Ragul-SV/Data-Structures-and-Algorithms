int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.empty())return 0;
        int m = matrix.size();
        int n = matrix[0].size();
        int res=0;
        int height[n],left[n],right[n];
        fill_n(left,n,0);
        fill_n(height,n,0);
        fill_n(right,n,n);
        int cur_l,cur_r;
        for(int i=0;i<m;i++)
        {
            cur_l = 0;cur_r = n;
            for(int j=0;j<n;j++)
            {
                height[j] = (matrix[i][j]=='1')?height[j]+1:0;
            }
            for(int j=0;j<n;j++)
            {
                if(matrix[i][j]=='1')
                    left[j] = max(left[j],cur_l);
                else
                {
                    cur_l = j+1;
                    left[j] = 0;
                }
            }
            for(int j=n-1;j>=0;j--)
            {
                if(matrix[i][j]=='1')
                    right[j] = min(right[j],cur_r);
                else
                {
                    cur_r = j;
                    right[j] = n;
                }
            }
            for(int j=0;j<n;j++)
            {
                res = max(res,(right[j]-left[j])*height[j]);
            }
        }
        return res;
    }
