import sys 
sys.setrecursionlimit(1000000000)
INF = 1000000009
MAX = 100000 
parent = [0 for i in range(MAX + 5)]
ranks = [0 for i in range(MAX + 5)] 

class Triad:
	def __init__(self, source, target, weight):
		self.source = source
		self.target = target
		self.weight = weight	
	def __lt__(self, other): 
		if self.weight < other.weight:
			return True
		
		if self.weight == other.weight: 
			if (self.source < other.source) or (self.source == other.source and self.target < other.target): 
				return True 		
		return False

dist = []
graph = []

def makeSet(v):
	for i in range(v + 1): 
		parent[i] = i
		ranks[i] = 0
	
def findSet(u): 
	if parent[u] != u: 
		parent[u] = findSet(parent[u]) 
	return parent[u]
	
def unionSet(u, v):
	up = findSet(u)
	vp = findSet(v)
	if up == vp:
		return
	
	if ranks[up] > ranks[vp]:
		parent[vp] = up
	else:
		if ranks[up] < ranks[vp]:
			parent[up] = vp
		else:
			parent[up] = vp 
			ranks[vp] += 1

def ABS(x):
	if x < 0:
		x = -x
	return x

def calcMST():
	res = 0
	for i in range(len(dist)): 
		res += dist[i].weight	
	return res
		
def Kruskal(V): 
	graph.sort()
	i = 0
	min_demand = 0
	while (len(dist) != V - 1):
		edge = graph[i]
		i += 1
		u = findSet(edge.source)
		v = findSet(edge.target)
		if u != v:
			dist.append(edge)
			unionSet(u, v)
			min_demand += edge.weight

while True: 
	V, E = map(int, input().split(" ")) 
	if V == 0 and E == 0: 
		break 	
	graph.clear()
	dist.clear()
	max_demand = 0
	for e in range(E):
		u, v, w = map(int, input().split(" ")) 
		max_demand += w 
		tmp = Triad(u, v, w)
		graph.append(tmp)	
	makeSet(V)
	Kruskal(V)
	print(max_demand - calcMST())
