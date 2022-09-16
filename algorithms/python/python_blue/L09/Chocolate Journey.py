import queue
MAX = int(1e5) + 1
INF = int(1e9)

class Node:
    def __init__(self, id = 0, dist = 0):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()

        u = top.id 
        w = top.dist 
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist 
                pq.put(Node(v.id, dist[v.id]))

graph = [[] for i in range(MAX + 1)]
dist = [INF for i in range(MAX + 1)]
have_ch = [False for i in range(MAX + 1)]
n, m, k, t = map(int, input().split())
ch = list(map(int, input().split()))
for x in ch:
    have_ch = True

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(v, w))
    graph[v].append(Node(u, w))
a, b = map(int, input().split())

Dijkstra(a)
dist_A = []
for x in dist:
    dist_A.append(x)

dist = [INF for i in range(MAX + 1)]
Dijkstra(b)
res = INF
for x in ch:
    if dist[x] <= t and dist_A[x] + dist[x] < res:
        res = dist[x] + dist_A[x]

if res == INF:
    print(-1)
else:
    print(res)
