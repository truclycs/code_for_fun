import queue
INF = 10 ** 9

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id

    def __lt__(self, other):
        return self.dist < other.dist
    def __str__(self):
        return "%d %d" % (self.id, self.dist)

def prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while not pq.empty():
        u = pq.get().id
        visited[u] = True
        for neighbor in graph[u]:
            v, w = neighbor.id, neighbor.dist
            if not visited[v] and dist[v] > w:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u
    
    for u in range(2, C + 1):
        if path[u] != -1:
            v, w = path[u], dist[u]
            mstGraph[u].append(Node(v, w))
            mstGraph[v].append(Node(u, w))

def dfs(src, dst, level):
    if src == dst:
        return level
    visited[src] = True
    for neighbor in mstGraph[src]:
        v, w = neighbor.id, neighbor.dist
        if not visited[v]:
            tmpLevel = dfs(v, dst, max(level, w))
            if tmpLevel != INF:
                return tmpLevel
    return INF

Case = 0
while (True):
    C, S, Q = map(int, input().split())
    if C == S == Q == 0:
        break
    
    mstGraph = [[] for i in range(C + 1)]
    graph = [[] for i in range(C + 1)]
    visited = [False] * (C + 1)
    dist = [INF] * (C + 1)
    path = [-1] * (C + 1)

    for i in range(S):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    for i in range(1, C + 1):
        if not visited[i]:
            prim(i)

    Case += 1
    print('Case #' + str(Case))
    for i in range(Q):
        u, v = map(int, input().split())
        visited = [False] * (C + 1)
        level = dfs(u, v, 0)
        print(level if level < INF else 'no path')