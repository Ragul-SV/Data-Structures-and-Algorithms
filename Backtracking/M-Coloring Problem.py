#------------------------------------O(k^V)-----------------------------------------#
def isSafe(graph,V,v,colors,c):
    for i in range(V):
        if graph[v][i]==1 and colors[i]==c:
            return False
    return True
    
def graphColoringUtil(graph,k,V,colors,v):
    if v==V:
        return True
    for c in range(1,k+1):
        if isSafe(graph,V,v,colors,c):
            colors[v] = c
            if graphColoringUtil(graph,k,V,colors,v+1):
                return True
            colors[v] = 0

def graphColoring(graph, k, V):
    '''
    :param graph: grid of size V*V in specified format(0 based indexing i.e. vertex 1 is index 0)
    :param k: number of colors allowed
    :param V: number of vertices 
    :return: True or False
    '''
    colors = [0]*V
    if graphColoringUtil(graph,k,V,colors,0)==None:
        return False
    return True
