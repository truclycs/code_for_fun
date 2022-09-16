import sys
sys.setrecursionlimit(1000000000)
INF = 1000000009
MAX = 100000

parent = [0 for i in range(MAX + 5)]
ranks = [0 for i in range(MAX + 5)]
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

def printMST():
    ans = 0
    for i in range(len(dist)):
        print(chr(dist[i].source + 65), end = "-")
        print(chr(dist[i].target + 65), end = " ")
        print(dist[i].weight)
        ans += dist[i].weight

def Kruskal(V):
    graph.sort()
    i = 0
    while (len(dist) != V - 1):
        edge = graph[i]
        i += 1
        u = findSet(edge.source)
        v = findSet(edge.target)
        if u != v:
            dist.append(edge)
            unionSet(u, v)

T = int(input())
for t in range(T):
    V = int(input())
    graph.clear()
    dist.clear()
    for i in range(V):
        st = list(map(int, input().replace(',','').split()))
        for j in range(V):
            if i < j and st[j] != 0:
                e = Triad(i, j, st[j])
                graph.append(e)
    print("Case {}:".format(t + 1))
    makeSet(V)
    Kruskal(V)
    printMST()
