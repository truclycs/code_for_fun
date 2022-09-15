import queue
INF = 1e9
MAX = 100001

class Node:     
    def __init__(self, dist, id):         
        self.dist = dist         
        self.id = id       
    def __lt__(self, other):         
        return self.dist < other.dist 

def Prim(src):     
    pq = queue.PriorityQueue()     
    pq.put(Node(0, src))     
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
                pq.put(Node(w, v))    
                path[v] = u

def printMST():
    global q
    global c
    global dist
    x = 0
    y = 0
    res = [0] * MAX
    for i in range(1, n + 1):
        if path[i] == -1:
            continue
        res[x] = dist[i]
        x += 1

    ans = 0
    res = res[0:x]
    res.sort()
    for i in range(x - 1, -1, -1):
        if res[i] > c[y] and y < q:
            ans += c[y]
            y += 1
        else:
            ans += res[i]
    print(ans)


n, m = map(int, input().split())
graph = [[] for i in range(n + 5)]
dist = [INF for i in range(n + 5)]
visited = [False for i in range(n + 5)]
path = [-1 for i in range(n + 5)]  

for i in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Node(w, v))
    graph[v].append(Node(w, u))

q = int(input())
c = [0] * MAX
if q != 0:
    c = list(map(int, input().split()))
    c.sort()
Prim(1)
printMST()
