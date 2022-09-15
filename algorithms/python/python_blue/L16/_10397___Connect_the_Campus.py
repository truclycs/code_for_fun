import queue
INF = 10 ** 9

class node:
    def __init__(self, dist, id):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist < other.dist

def prim(src):
    dist = [INF for i in range(n)]
    visited = [0 for i in range(n)]
    total = 0
    dist[src] = 0
    Q = queue.PriorityQueue()
    Q.put(node(0, src))
    trace = [{} for i in range(n)]
    while not Q.empty():
        top = Q.get()
        u = top.id
        d = top.dist
        visited[u] = True
        i = 0
        for neighbor in graph[u]:    
            v = neighbor.id             
            w = neighbor.dist 
            if not visited[v] and dist[v] > w:
                dist[v] = w
                Q.put(node(dist[v], v))
                trace[v] = {'p': u, 'id': i}
            i += 1

    for i in range(n):
        total += dist[i]
    return total, trace

T = int(input())
while T:
    T -= 1
    n, m = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v, cost = map(int, input().split())
        graph[u - 1].append(node(cost, v - 1))
        graph[v - 1].append(node(cost, u - 1))
        trace = []
        min1, trace = prim(0)
        min2 = INF

    for j in range(1, n):
        item = trace[j]         
        u = item['p']
        i = item['id']
        temp = graph[u][i].dist
        graph[u][i].dist = INF
        val, temp_trace = prim(0)
        graph[u][i].dist = temp
        min2 = min(min2, val)

    print('{} {}'.format(min1, min2))
