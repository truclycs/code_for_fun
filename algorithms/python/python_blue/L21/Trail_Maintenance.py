class Triad:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight
    
def find(u):
    if u != par[u]:
        par[u] = find(par[u])
    return par[u]

def union(u, v):
    u = find(u)
    v = find(v)
    if u == v:
        return
    if rank[u] > rank[v]:
        par[v] = u
    elif rank[u] < rank[v]:
        par[u] = v
    else:
        par[u] = v
        rank[v] += 1

def Kruskal(V):
    global par, rank
    par = [i for i in range(V + 1)]
    rank = [0 for i in range(V + 1)]
    nEdge = res = 0
    delpos = -1
    for i, edge in enumerate(graph):
        u = find(edge.source)
        v = find(edge.target)
        if u != v:
            res += edge.weight
            union(u, v)
            nEdge += 1
        else:
            delpos = i
    if delpos >= 0:
        graph.pop(delpos)
    return res if nEdge == V - 1 else -1

Case = 0
T = int(input())
while (T):
    T -= 1
    Case += 1
    print("Case " + str(Case))
    n, w = map(int, input().split())
    graph = []
    for i in range(w):
        u, v, w = map(int, input().split())
        graph.append(Triad(u - 1, v - 1, w))
        for i in range(len(graph) - 1, 0, -1):
            if graph[i].weight < graph[i - 1].weight:
                graph[i], graph[i - 1] = graph[i - 1], graph[i]
            else:
                break
        print(Kruskal(n))

