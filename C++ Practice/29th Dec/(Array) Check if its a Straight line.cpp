bool checkStraightLine(vector<vector<int>>& arr) {
        int n = arr.size();
        if(n==2)return true;
        int dy = (arr[1][1]-arr[0][1]);
        int dx = (arr[1][0]-arr[0][0]);
        int x1 = arr[0][0],y1 = arr[0][1];
        int x,y;
        for(int i=2;i<n;i++)
        {
            x = arr[i][0];
            y = arr[i][1];
            if(dx*(y-y1)!=dy*(x-x1))
                return false;
        }
        return true;
    }
