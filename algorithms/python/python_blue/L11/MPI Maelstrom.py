MAX = 101
INF = int(1e9)

class Triad:
	def __init__(self, source, target, weight):
	    self.source = source
	    self.target = target
	    self.weight = weight
 
def BellmanFord(s):
	dist[s] = 0
	for i in range(1, n):
		for j in range(m):
			u = graph[j].source
			v = graph[j].target
			w = graph[j].weight
			if dist[u] != INF and dist[u] + w < dist[v] :
				dist[v] = dist[u] + w
		
m = 0
dist = []
dist = [INF for i in range(MAX + 1)]
graph = [] 
n = int(input())
for i in range(2, n + 1):
    w = input().split()
    for j in range(0, i - 1):
        if w[j] != "x":
            m += 2
            graph.append(Triad(i, j + 1, int(w[j])))
            graph.append(Triad(j + 1, i, int(w[j])))

BellmanFord(1)
res = 0
for i in range(1, n + 1):
    res = max(res, dist[i])
print(res)
