def dfs(graph,v,visited,parent):
    visited[v] = True
    if v in graph:
        for i in graph[v]:
            if visited[i]==False:
                if dfs(graph,i,visited,v):
                    return True
            elif parent!=i:
                return True
    return False

def isCyclic(graph,n):
    visited = [False]*n
    for i in range(n):
        if visited[i]==False:
            if dfs(graph,i,visited,-1)==True:
                return 1
    return 0
