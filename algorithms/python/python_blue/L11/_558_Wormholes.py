INF = 10**9

class Edge:
    def __init__(self, s, t, w):
        self.s = s
        self.t = t
        self.w = w

def BellmanFord(n):
    dist = [INF] * n
    dist[0] = 0
    for i in range(n - 1):
        for j in range(m):
            u = graph[j].s
            v = graph[j].t
            w = graph[j].w
            if dist[u] != INF and dist[u] + w < dist[v]:
                if i == n - 2:
                    return False
                dist[v] = dist[u] + w
    return True

t = int(input())
for T in range(t):
    n, m = map(int, input().split())
    graph = []
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w));

    if not BellmanFord(n):
        print("possible")
    else:
        print("not possible")
