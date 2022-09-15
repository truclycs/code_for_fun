INF = 10 ** 9
import queue

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
            dist[e.v] = -INF

while True:
    n, m, q, s = map(int, input().split())
    if n == m == q == s == 0:
        break
    graph = []
    dist = [INF] * n
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append(Edge(u, v, w))
    
    BellmanFord(s)
    for i in range(q):
        t = int(input())
        if dist[t] == INF:
            print("Impossible")
        elif dist[t] == -INF:
            print("-Infinity")
        else: 
            print(dist[t])           
    print()