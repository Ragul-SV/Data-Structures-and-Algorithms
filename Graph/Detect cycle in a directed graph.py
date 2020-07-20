def dfs(graph,v,visited,st):
    visited[v] = True
    st[v] = True
    if v in graph:
        for i in graph[v]:
            if visited[i]==False:
                if dfs(graph,i,visited,st):
                    return True
            elif st[i]==True:
                return True
    st[v] = False
    return False
                
def isCyclic(n, graph):
    visited = [False]*n
    st = [False]*n
    for i in range(n):
        if visited[i]==False:
            if dfs(graph,i,visited,st)==True:
                return True
    return False
