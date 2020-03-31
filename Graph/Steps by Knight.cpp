#include <bits/stdc++.h>
using namespace std;

bool safe(int x,int y,int n)
{
    return x>=1 && x<=n && y>=1 && y<=n;
}

int main() {
	int t,n,x1,y1,x2,y2,i,j,count,size,flag,x,y;
	cin>>t;
	int dx[] = {2,2,-2,-2,1,1,-1,-1};
	int dy[] = {1,-1,1,-1,2,-2,2,-2};
	while(t--)
	{
	    cin>>n;
	    cin>>x1>>y1;
	    cin>>x2>>y2;
	    int dp[n+1][n+1];
	    for(i=0;i<n+1;i++)
	    {
	        for(j=0;j<n+1;j++)
	        {
	            dp[i][j] = INT_MAX;
	        }
	    }
	    queue<pair<int,int>> q;
	    q.push({x1,y1});
	    int count = 0;
	    while(!q.empty())
	    {
	        size = q.size();
	        flag = 0;
	        while(size--)
	        {
	            pair<int,int> p = q.front();
	            q.pop();
	            for(i=0;i<8;i++)
	            {
	                x = p.first + dx[i];
	                y = p.second + dy[i];
	                if(safe(x,y,n))
	                {
	                    if((count+1)<dp[x][y])
	                    {
	                        flag = 1;
	                        dp[x][y] = count + 1;
	                        q.push({x,y});
	                    }
	                }
	            }
	        }
	        if(flag) count++;
	    }
	    if(x1==x2 && y1==y2) dp[x2][y2] = 0;
	    if(dp[x2][y2]==INT_MAX) dp[x2][y2] = 1;
	    cout<<dp[x2][y2]<<endl;
	}
}
