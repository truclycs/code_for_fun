INF = 10 ** 9

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def BellmanFord():
    pro = [-1] * (n + 1)
    pro[1] = 1.0
    for i in range(n - 1):
        for e in graph:
            pro[e.u] = max(pro[e.u], pro[e.v] * e.w)
            pro[e.v] = max(pro[e.v], pro[e.u] * e.w)
    return pro[n] * 100.0

while True:
    l = list(map(int, input().split()))
    if len(l) == 1:
        break
    n = l[0]
    m = l[1]
    graph = []
    dist = [INF] * (n + 1)
    for i in range(m):
        a, b, p = map(int, input().split())
        graph.append(Edge(a, b, p / 100.0))
    print("{:.6f} percent".format(BellmanFord()))

