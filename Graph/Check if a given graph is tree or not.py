from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u-1].append(v-1)
        self.graph[v-1].append(u-1)

def isCycle(graph,v,visited,parent):
    visited[v] = True
    for i in graph[v]:
        if visited[i]==False:
            if isCycle(graph,i,visited,v)==True:
                return True
        elif i!=parent:
            return True
    return False
        
def isTree(n,m,arr):
    g = Graph(n)
    for i in range(m):
        g.addEdge(arr[i][0],arr[i][1])
    visited = [False]*n
    if isCycle(g.graph,0,visited,-1)==True:
        return False
    for i in range(n):
        if visited[i]==False:
            return False
    return True
