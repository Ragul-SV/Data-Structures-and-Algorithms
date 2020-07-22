import sys
sys.setrecursionlimit(10000000)
def topoSortUtil(adj,v,visited,stack):
    visited[v] = True
    for i in adj[v]:
        if visited[i]==False:
            topoSortUtil(adj,i,visited,stack)
    stack.insert(0,v)
    
def topoSort(n, adj):
    visited = [False]*n
    stack = []
    for i in range(n):
        if visited[i]==False:
            topoSortUtil(adj,i,visited,stack)
    return stack
