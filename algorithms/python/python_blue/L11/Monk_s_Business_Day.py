INF = 10 ** 9

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def BellmanFord(s):
    dist[s] = 0
    for i in range(n - 1):
        for e in graph:
            if dist[e.u] != INF and dist[e.u] + e.w < dist[e.v]:
                dist[e.v] = dist[e.u] + e.w
    for e in graph:
        if dist[e.u] != INF and dist[e.u] + e.w < dist[e.v]:
            return False
    return True
        
t = int(input())
while t:
    t -= 1
    n, m = map(int, input().split())
    graph = []
    dist = [INF] * (n + 1)
    for i in range(m):
        i, j, c = map(int, input().split())
        graph.append(Edge(i, j, -c))

    if BellmanFord(1):
        print("No")
    else:
        print("Yes")
