#include <bits/stdc++.h>
using namespace std;
#define R 4 
#define C 4 

int knapsack(int val[],int wt[],int W,int n)
{
	int dp[n+1][W+1];
	
	for(int i=0;i<n+1;i++)
	{
		for(int j=0;j<W+1;j++)
		{
			if(i==0 || j==0)dp[i][j] = 0;
			else if(j>=wt[i-1])
			{
				dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j]);
			}
			else
			dp[i][j] = dp[i-1][j];
		}
		for(int i=0;i<=n;i++)
	{
		for(int j=0;j<=W;j++)
		{
			cout<<dp[i][j]<<" ";
		}
		cout<<endl;
	}
	}
	return dp[n][W];
}

int main() {
	int m = 4,n = 4;
	int arr[m][n] = { { 1, 2, 3, 4 }, 
                    { 5, 6, 7, 8 }, 
                    { 9, 10, 11, 12 }, 
                    { 13, 14, 15, 16 } }; 
  
    int i,j,start_row = 0,start_col = 0;
    while(start_row<m && start_col<n)
    {
    	for(j=start_col;j<n;j++)
    	{
    		cout<<arr[start_row][j]<<" ";
    	}
    	start_row++;
    	for(i=start_row;i<m;i++)
    	{
    		cout<<arr[i][n-1]<<" ";
    	}
    	n--;
    	if(start_row<m)
    	{
    		for(j=n-1;j>=start_col;j--)
    		{
    			cout<<arr[m-1][j]<<" ";
    		}
    		m--;
    	}
    	
    	if(start_col<n)
    	{
    		for(i=m-1;i>=start_row;i--)
    		{
    			cout<<arr[i][start_col]<<" ";
    		}
    		start_col++;
    	}
    	
    }
    return 0;
}
