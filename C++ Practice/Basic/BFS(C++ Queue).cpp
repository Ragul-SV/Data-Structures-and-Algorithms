#include <bits/stdc++.h>
using namespace std;

class Graph
{
	int V;
	list<int> *adj;
	
	public:
	Graph(int V)
	{
		this->V = V;
		adj = new list<int>[V];
	}
	
	void addEdge(int u,int v)
	{
		adj[u].push_back(v);
	}
	
	void BFS(int u)
	{
		bool *visited = new bool[V];
		for(int i=0;i<V;i++)
		{
			visited[i] = false;
		}
		visited[u] = true;
		queue<int> q;
		q.push(u);
		while(!q.empty())
		{
			int temp = q.front();
			cout<<temp<<" ";
			q.pop();
			for(list<int>::iterator i=adj[temp].begin();i!=adj[temp].end();i++)
			{
				if(!visited[*i])
				{
					visited[*i] = true;
					q.push(*i);
				}
			}
		}
		cout<<endl;
	}
};

int main()  
{  
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    
    g.BFS(2);
}
