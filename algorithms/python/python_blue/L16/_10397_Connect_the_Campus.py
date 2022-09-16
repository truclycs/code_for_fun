import queue
import math
INF =  1e9
 
class Scanner:
    def __generator__():
        while True:
            try:
                buff = input().strip().split()
                for x in buff:
                    yield x
            except EOFError:
                exit()
 
    sc = __generator__()
    def next():
        return Scanner.sc.__next__()
 
class Node:     
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist          
    def __lt__(self, other):         
        return self.dist < other.dist 
 
def totalWeight():     
    res = 0     
    for i in range(n):         
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
        visited[u] = True         
        for neighbor in graph[u]:     
            v = neighbor.id           
            w = neighbor.dist             
            if not visited[v] and w < dist[v]:                 
                dist[v] = w                 
                pq.put(Node(v, w))    
                path[v] = u
 
 
def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
 
while True:
    n = int(Scanner.next())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = int(Scanner.next()), int(Scanner.next())
 
    graph = [[] for i in range(n + 1)]     
    dist = [INF for i in range(n + 1)]     
    path = [-1 for i in range(n + 1)]     
    visited = [False for i in range(n + 1)] 
 
    for i in range(n):
        for j in range(n):
            graph[i].append(Node(j, distance(x[i], y[i], x[j], y[j])))
            
    m = int(Scanner.next())
    for i in range(m):
        u, v = int(Scanner.next()), int(Scanner.next())
        u -= 1
        v -= 1
        graph[u][v] = Node(v, 0)
        graph[v][u] = Node(u, 0)
 
    Prim(0)
    print('{:.2f}'.format(totalWeight()))

