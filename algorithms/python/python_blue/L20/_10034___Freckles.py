import queue
INF = 1e9
MAX = 101

class Node:
    def __init__(self, id, dist):
        self.dist = dist
        self.id = id
    def __lt__(self, other):
        return self.dist <= other.dist

def Prim(src):
    pq = queue.PriorityQueue()
    pq.put(Node(src, 0))
    dist[src] = 0
    while pq.empty() == False:
        top = pq.get()
        u = top.id
        d = top.dist
        visited[u] = True
        for neighbor in graph[u]:
            v = neighbor.id
            w = neighbor.dist
            if visited[v] == False and w < dist[v]:
                dist[v] = w
                pq.put(Node(v, w))
                path[v] = u

def printMST():
    res = 0
    for i in range(n):
        if path[i] == -1:
            continue
        res += dist[i]
    print("{0:.2f}".format(res))

T = int(input())
while (T):
    T -= 1
    s = input()
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(float, input().split())
        x.append(a)
        y.append(b)
    path = [-1 for i in range(MAX)]
    visited = [False for i in range(MAX)]
    graph = [[] for i in range(MAX)]
    dist = [INF for i in range(MAX)]
    for i in range(n):
        for j in range(n):
            w = ((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5
            graph[i].append(Node(j, w))
            graph[j].append(Node(i, w))
    Prim(0)
    printMST()
    if T:
        print()
