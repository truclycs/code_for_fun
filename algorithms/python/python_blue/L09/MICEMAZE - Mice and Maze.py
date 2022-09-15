import queue
MAX = 1001
INF = int(1e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist 


def Dijkstra(s):
    res = 0
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    res = 1
    while not pq.empty():
        top = pq.get()
        u = top.id 
        w = top.dist 
        for v in graph[u]:
            if w + v.dist < dist[v.id]:
                dist[v.id] = w + v.dist 
                if dist[v.id] <= t:
                    res += 1
                    pq.put(Node(v.id, dist[v.id]))
    return res            

graph = [[] for i in range(MAX + 1)]
dist = [INF for i in range(MAX + 1)]

n = int (input())
e = int (input())
t = int (input())
m = int (input())
for i in range(m):
    u, v, w = map(int, input().split())
    graph[v].append(Node(u, w))

print(Dijkstra(e))


    
