import queue
INF = -10**9

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def BFS(s, t, graph):
    visited = [False] * (t + 1)
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    if s == t:
        return True
    while not q.empty():
        u = q.get()
        for e in graph:
            if e.u == u and not visited[e.v]:
                visited[e.v] = True
                if e.v == t:
                    return True
                q.put(e.v)
    return False

def BellmanFord(n, graph):
    dist = [INF] * (n + 1)
    dist[1] = 100
    for i in range(n - 1):
        for e in graph:
            if dist[e.u] <= 0:
                continue
            if dist[e.u] + e.w > dist[e.v]:
                dist[e.v] = dist[e.u] + e.w

    for e in graph:
        if dist[e.u] <= 0:
            continue
        if dist[e.u] + e.w > dist[e.v] and BFS(e.u, n, graph):
            return True
    if dist[n] > 0:
        return True
    else:
        return False

while True:
    n = int(input())
    if n == -1:
        break
    graph = []
    for i in range(n):
        a = list(map(int, input().split()))
        for x in a[2:]:
            graph.append(Edge(i + 1, x, a[0]))
    if BellmanFord(n, graph):
        print("winnable")
    else:
        print("hopeless")