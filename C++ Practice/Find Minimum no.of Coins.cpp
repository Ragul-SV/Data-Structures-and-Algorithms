#include <bits/stdc++.h>
using namespace std;

int minCoins(int coins[],int m,int V)
{
	int dp[V+1];
	dp[0] = 0;
	for(int i=1;i<V+1;i++)
	{
		dp[i] = INT_MAX;
	}
	for(int i=1;i<V+1;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(coins[j]<=i)
			{
				int temp = dp[i-coins[j]];
				if(temp!=INT_MAX && temp+1<dp[i])
				dp[i] = temp + 1;
			}
		}
	}
	return dp[V];
}

int main() {
	int coins[] =  {9, 6, 5, 1}; 
    int m = sizeof(coins)/sizeof(coins[0]); 
    int V = 11; 
    cout << "Minimum coins required is "
         << minCoins(coins, m, V); 
    return 0; 
}
