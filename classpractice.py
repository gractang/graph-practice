import sys

class Vertex:

	# color is some number, with 0 being uncolored
	def __init__(self, name, color=0):
		self.name = name
		self.color = color

	def __repr__(self):
		return str(self.name)

class Edge:
	def __init__(self, v1, v2, weight=1):
		self.v1 = v1
		self.v2 = v2
		self.weight = weight

	def __repr__(self):
		return "\nedge: " + self.v1.name + ":" + str(self.v1.color) + " " + self.v2.name + ":" + str(self.v2.color) + " weight:" + str(self.weight)

class Graph:

	# V is set of vertices, E is set of edges
	def __init__(self, V, E):
		self.V = V
		self.E = E

	def __repr__(self):
		string = ""
		for edge in self.E:
			string += str(edge)
		return string

	def Neighbors(self, v):
		adjacents = set()
		for edge in self.E:
			if edge.v1 == v:
				adjacents.add(edge.v2)
			elif edge.v2 == v:
				adjacents.add(edge.v1)
		return adjacents

	def MinEdge(self, v):
		# largest integer value
		min_weight = sys.maxsize
		min_edge = None
		for edge in self.E:
			if edge.weight < min_weight and (edge.v1 == v or edge.v2 == v):
				min_weight = edge.weight
				min_edge = edge
		return min_edge

	def RemoveEdge(self, e):
		self.E.remove(e)

	def RemoveVertex(self, v):
		self.V.remove(v)
		for edge in self.E:
			if edge.v1 == v or edge.v2 == v:
				self.E.remove(edge)

	def ChromaticNumber(self):
		num_distinct = set()
		for vertex in self.V:
			if vertex.color == 0:
				print("lmao ur bad the graph isn't done coloring yet")
				return None
			else:
				num_distinct.add(vertex.color)
		return len(num_distinct)

	def IsValidColoring(self):
		for edge in self.E:
			if edge.v1.color == 0 or edge.v2.color == 0:
				print("lmao ur bad the graph isn't done coloring yet")
				return None
			if edge.v1.color == edge.v2.color:
				return False
		return True

	def GreedyColor(self):
		for vertex in self.V:
			distinct_colors = set()
			adjacents = self.Neighbors(vertex)
			for adj in adjacents:
				distinct_colors.add(adj.color)
			for i in range(1,len(self.V)):
				if i not in distinct_colors:
					vertex.color = i
					break

	# not done
	def BruteForce(self):
		for i in range(len(self.V)):
			for vertex in self.V:
				distinct_colors = set()
				adjacents = self.Neighbors(vertex)

	# Optional problems!!

	def DFS(self, start_vertex, target_vertex):
		pass

	def IsTree(self):
		pass

	def IsPlanar(self):
		pass

	def SpanningTree(self):	
		discovered = set()
		T = set()
		frontier = [next(iter(self.V))]
		while frontier:
			v = frontier.pop()
			discovered.add(v)
			neighbors = self.Neighbors(v)
			for neighbor in neighbors:
				if neighbor not in visited:
					T.add(Edge(v, neighbor))
					frontier.insert(0, neighbor)
		return T

	def PrimMST(self):
		T = set()
		discovered = set()
		frontier = [next(iter(self.V))]
		while frontier:
			v = frontier.pop()
			neighbors = self.Neighbors(v)
			for neighbor in neighbors:

		

vert = Vertex("a")
ver = Vertex("b")
ve = Vertex("c")
v = Vertex("d")
ed = Edge(vert, ver, 42)
edg = Edge(v, ver, 7)
edgy = Edge(ver, ve)

print(vert)
print(ed)
print(edgy)
V = {vert, ver, ve, v}
E = {ed, edg, edgy}
gra = Graph(V, E)
print(gra.Neighbors(ve))
print(gra.MinEdge(ver))
print(gra.ChromaticNumber())
print(gra.IsValidColoring())
gra.GreedyColor()
print(gra)
