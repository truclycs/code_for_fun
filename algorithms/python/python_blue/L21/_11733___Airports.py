class Triad:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

parent = []
ranks = []
dist = []
graph = []

def makeSet(V):
    global parent, ranks
    parent = [i for i in range(V + 1)]
    ranks = [0 for i in range(V + 1)]

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
        parent[up] = vp
        ranks[vp] += 1

def Kruskal(M, N, A):
    global graph, countAirports
    graph.sort(key = lambda edge: edge.weight)
    i = 0
    for edge in graph:
        if edge.weight >= A:
            break
        u = findSet(edge.source)
        v = findSet(edge.target)
        if  u != v:
            dist.append(edge)
            unionSet(u, v)
            countAirports -= 1
            if countAirports == 1:
                break

T = int(input())
Case = 0
while T:
    T -= 1
    N, M, A = map(int, input().split())
    for i in range(M):
        u, v, w = map(int, input().split())
        graph.append(Triad(u, v, w))

    countAirports = N
    res = 0
    makeSet(N)
    Kruskal(M, N, A)
    for x in dist:
        res += x.weight
    
    Case += 1
    print("Case # " + str(Case) + ": " + str(res + countAirports * A) + " " + str(countAirports))
    graph.clear()
    dist.clear()