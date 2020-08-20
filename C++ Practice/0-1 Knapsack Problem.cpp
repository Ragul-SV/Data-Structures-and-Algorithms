#include <bits/stdc++.h>
using namespace std;

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
	 int val[] = { 10, 20, 30 }; 
    int wt[] = { 1, 1, 1 }; 
    int W = 2;
    int n = sizeof(val)/sizeof(val[0]);
    cout<<knapsack(val,wt,W,n);
    return 0;
}
