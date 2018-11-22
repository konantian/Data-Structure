class Graph:
	def __init__(self,graph_dict={}):
		self.graph=graph_dict

	def vertices(self):
		return list(self.graph.keys())

	def edges(self):
		return self.__generate_edges()

	def add_vertex(self,vertex):
		if vertex not in self.graph:
			self.graph[vertex]=[]

	def add_edge(self,edge):
		edge=set(edge)
		(vertex1,vertex2)=tuple(edge)
		if vertex1 in self.graph:
			self.graph[vertex1].append(vertex2)
		else:
			self.graph[vertex1]=[vertex2]

	def BFS(self,s):
		values=[False]*len(self.graph)
		visited=dict(zip(self.vertices(),values))
		queue=[]

		queue.append(s)
		visited[s]=True

		while queue:
			s=queue.pop(0)
			print(s,end=' ')

			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i]=True
		print()

	def DFS(self,v):
		value=[False]*len(self.graph)
		visited=dict(zip(self.vertices(),value))

		self.DFSUtil(v,visited)
		print()

	def DFSUtil(self,v,visited):

		visited[v]=True
		print(v,end=' ')

		for i in self.graph[v]:
			if visited[i] == False:
				self.DFSUtil(i,visited)

	def isCyclic(self):
		visited=[False]*5
		#recStack=[False]*len(self.graph)

		for node in range(5):
			if visited[node]==False:
				if self.isCyclicUtil(node,visited,-1) == True:
					return True
		return False

	def isCyclicUtil(self,v,visited,parent):
		visited[v]=True
		#recStack[v]=True

		for neighbour in self.graph[v]:
			if visited[neighbour]==False:
				if self.isCyclicUtil(neighbour,visited,v)==True:
					return True
			elif parent != neighbour:
				return True

		#recStack[v]=False
		return False


	def __generate_edges(self):
		edges=[]

		for vertex in self.graph:
			for neighbour in self.graph[vertex]:
				if {neighbour,vertex} not in edges:
					edges.append({vertex,neighbour})
		return edges

	def __str__(self):
		res="vertices: "
		for k in self.graph:
			res+=str(k)+" "
		res+="\nedges: "
		for edge in self.__generate_edges():
			res+=str(edge)+" "

		return res

if __name__ == "__main__":

	g1={0:[1],
	   1:[2,3],
	   2:[3,4],
	   3:[4,5],
	   4:[4],
	   5:[6,7],
	   6:[8],
	   7:[7],
	   8:[8]}

	g2={"A":["B","C"],
		"B":["A","E","D"],
		"C":["A","E"],
		"D":["B","E","F"],
		"E":["C","B","D","F"],
		"F":["D","E"]}

	g3={0:[1,2],
		1:[2],
		2:[0,3],
		3:[3]}


	graph = Graph()
	graph.add_edge({1,0})
	graph.add_edge({0,2})
	graph.add_edge({2,0})
	graph.add_edge({0,3})
	graph.add_edge({3,4})
	#print(graph)
	#graph.DFS(0)
	print(graph.isCyclic())


