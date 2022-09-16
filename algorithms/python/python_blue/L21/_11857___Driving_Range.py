import sys
sys.setrecursionlimit(100000000)
MAXN = 100005
parent = []
ranks = []

class Triad:
    def __init__(self, target, source, weight):
        self.target = target
        self.source = source
        self.weight = weight

def makeSet(V):
    global parent, ranks
    parent = [i for i in range(V + 1)]
    ranks = [0 for i in range(V + 1)]

def findSet(u):
    if parent[u] != u:
        parent[u] = findSet(parent[u])
    return parent[u]

def unionSet(u, v):
    if u == v:
        return
    if ranks[u] > ranks[v]:
        parent[v] = u
    elif ranks[u] < ranks[v]:
        parent[u] = v
    else:
        ranks[u] += 1
        parent[v] = u

def Kruskal(V, E):
    graph.sort(key = lambda Triad: Triad.weight)
    MST = 0
    i = 0
    maxEdge = -1
    while MST != V - 1 and i < E:
        u = findSet(graph[i].source)
        v = findSet(graph[i].target)
        if u != v:
            MST += 1
            if maxEdge < graph[i].weight:
                maxEdge = graph[i].weight
            unionSet(u, v)
        i += 1
    if MST == V - 1:
        return maxEdge
    return -1


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    makeSet(n)
    graph = []
    for i in range(m):
        source, target, weight = map(int, input().split())
        graph.append(Triad(target, source, weight))

    res = Kruskal(n, m)
    if res == -1:
        print("IMPOSSIBLE")
    else:
        print(res)   
