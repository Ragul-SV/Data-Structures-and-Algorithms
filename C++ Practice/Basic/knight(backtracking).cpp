#include <bits/stdc++.h>
using namespace std;
#define N 8

bool knightUtil(int x,int y,int move,int res[N][N],int nextx[N],int nexty[N]);

void printsol(int res[N][N])
{
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			cout<<setw(2)<<res[i][j]<<" ";
		}
		cout<<endl;
	}
}

void knight()
{
	int res[N][N];
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			res[i][j] = -1;
		}
	}
	int nextx[N] = {2,1,2,-1,1,-2,-2,-1};
	int nexty[N] = {1,2,-1,2,-2,1,-1,-2};
	res[0][0] = 0;
	if(knightUtil(0,0,1,res,nextx,nexty)==true) printsol(res);
	else cout<<"Solution does not exist";
}

bool safe(int x1,int y1,int res[N][N])
{
	return (x1>=0 && x1<N && y1>=0 && y1<N && res[x1][y1]==-1);
}

bool knightUtil(int x,int y,int move,int res[N][N],int nextx[N],int nexty[N])
{
	int x1,y1;
	if(move==N*N)
	return true;
	
	for(int k=0;k<8;k++)
	{
		x1 = x+nextx[k];
		y1 = y+nexty[k];
		if(safe(x1,y1,res))
		{
			res[x1][y1] = move;
			if(knightUtil(x1,y1,move+1,res,nextx,nexty)==true)
				return 1;
			else res[x1][y1] = -1;
		}
	}
	return false;
}

int main()  
{  
	knight();
	return 0;
}
