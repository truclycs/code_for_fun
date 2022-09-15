import sys 
sys.setrecursionlimit(1000000000) 
INF = 1000000009
MAX = 100001    
dist = []
graph = [] 

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

def makeSet(v):
    global parent, ranks
    parent = [i for i in range(v + 1)]
    ranks = [0 for i in range(v + 1)] 
 
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
            
def calcMST():
	res = 0
	for i in range(len(dist)): 
		res += dist[i].weight 
	return res

def Kruskal(V): 
	graph.sort()
	i = 0
	while (len(dist) != V - 1 and i < len(graph)):
		edge = graph[i]
		i += 1
		u = findSet(edge.source)
		v = findSet(edge.target)
		if u != v:
			dist.append(edge)
			unionSet(u, v)
            
def minPrice(s):
    makeSet(s)
    Kruskal(s)
    for i in range(1, s):
        u = findSet(0)
        v = findSet(i)
        if u != v:
            return -1 
    sum = 0
    for i in range(len(dist)):
        sum += dist[i].weight
    return sum
 
while True:
    S, C = map(int, input().split(' '))
    if S == C == 0:
        break
    graph.clear()
    dist.clear()
    
    station = dict()
    for i in range(S): 
        name = input()
        station[name] = i
 
    for i in range(C):
        st = list(input().split(' '))
        source = st[0]
        des = st[1]
        d = int(st[2])
        graph.append(Triad(station[source], station[des], d))
 
    name = input()
    res = minPrice(S)
    if res != -1:
        print(res)
    else:
        print("Impossible")
