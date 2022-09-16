import queue 
 
INF = 1e9 
 
class Node:     
    def __init__(self, id, dist):         
        self.dist = dist         
        self.id = id       
    def __lt__(self, other):         
        return self.dist <= other.dist 

def totalWeight():     
    res = 0     
    for i in range(1, n + 1):         
        if path[i] == -1:             
            continue         
        res += dist[i]         
    return res

def Prim(src):     
    pq = queue.PriorityQueue()     
    pq.put(Node(src, 0))     
    dist[src] = 0     
    while not pq.empty():         
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

n, m = map(int, input().split())     
graph = [[] for i in range(n + 1)]     
dist = [INF for i in range(n + 1)]     
path = [-1 for i in range(n + 1)]     
visited = [False for i in range(n + 1)]     
for i in range(m):         
    u, v, w = map(int, input().split())         
    graph[u].append(Node(v, w))         
    graph[v].append(Node(u, w))     
    
Prim(int(input()))

print(totalWeight())
