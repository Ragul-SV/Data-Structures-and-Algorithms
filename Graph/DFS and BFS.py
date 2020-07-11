class Graph:
	def __init__(self):
		self.graph = dict()
		
	def addEdge(self,u,v):
		if u not in self.graph:
			self.graph[u] = [v]
		else:
			self.graph[u].append(v)
	
	def DFSUtil(self,v,visited):
		visited.add(v)
		print(v,end=" ")
		if v in self.graph:
			for i in self.graph[v]:
				# print("v:",v,"i:",i)
				if i not in visited:
					self.DFSUtil(i,visited)
		
	def DFS(self,v):
		visited = set()
		self.DFSUtil(v,visited)
			
	def BFS(self,v):
		visited = set()
		queue = []
		queue.append(v)
		visited.add(v)
		while queue:
			cur = queue.pop(0)
			print(cur,end=" ")
			if cur in self.graph:
				for i in self.graph[cur]:
					if i not in visited:
						queue.append(i)
						visited.add(i)
	
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.DFS(2)
print()
g.BFS(2)
