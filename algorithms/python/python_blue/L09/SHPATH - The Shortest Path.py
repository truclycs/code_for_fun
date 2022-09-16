import queue
MAX = 10001
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

T = int(input())
while T:
    T -= 1
    graph = [[] for i in range(MAX + 1)]
    dist = [INF for i in range(MAX + 1)]
    n = int(input())
    city = {}
    for i in range(n):
        name = input()
        city[name] = i + 1
        p = int(input())
        for j in range(p):
            nr, cost = map(int, input().split())
            graph[i + 1].append(Node(nr, cost))
    r = int(input())
    for i in range(r):
        name1, name2 = input().split()
        s = city[name1]
        t = city[name2]
        Dijkstra(s)
        print(dist[t])