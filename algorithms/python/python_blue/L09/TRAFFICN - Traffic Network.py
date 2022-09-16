import heapq
MAX = 10001
INF = int(1e9)

class Node:
    def __init__(self, id = 0, dist = 0):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s, graph, dist):
    pq = []
    heapq.heappush(pq, (Node(s, 0)))
    dist[s] = 0
    while len(pq) > 0:
        top = pq[0]
        heapq.heappop(pq)
        u = top.id 
        w = top.dist 
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist 
                heapq.heappush(pq, (Node(v.id, dist[v.id])))

T = int(input())
while T:
    T -= 1
    n, m, k, s, t = map(int, input().split())
    graph_s = [[] for i in range(MAX + 1)]
    graph_t = [[] for i in range(MAX + 1)]
    dist_s = [INF for i in range(MAX + 1)]
    dist_t = [INF for i in range(MAX + 1)]
    for i in range(m):
        u, v, w = map(int, input().split())
        graph_s[u].append(Node(v, w))
        graph_t[v].append(Node(u, w))

    Dijkstra(s, graph_s, dist_s)
    Dijkstra(t, graph_t, dist_t)
    res = dist_s[t]
    for i in range(k):
        u, v, w = map(int, input().split())
        res = min(res, min(dist_s[u] + dist_t[v], dist_s[v] + dist_t[u]) + w)

    if res == INF:
        print(-1)
    else:
        print(res)

