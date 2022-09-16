import queue
MAX = 20001
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
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

N = int(input())
Case = 0
while N:
    N -= 1
    Case += 1
    graph = [[] for i in range(MAX + 1)]
    dist = [INF for i in range(MAX + 1)]
    n, m , S, T = map(int, input().split())
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append(Node(v, w))
        graph[v].append(Node(u, w))

    Dijkstra(S)
    if dist[T] != INF:
        print("Case #{}: {}".format(Case, dist[T]))
    else:
         print("Case #{}: unreachable".format(Case))


    
