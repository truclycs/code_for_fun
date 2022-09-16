from queue import Queue 
 
MAX = 1001

def BFS(s):
    for i in range(V + 1):
        visited[i] = False
        dist[i] = 0
    q = Queue()
    visited[s] = True
    q.put(s)
    while q.empty() == False:
        u = q.get()
        for v in graph[u]:
            if visited[v] == False:
                visited[v] = True
                q.put(v)
                dist[v] = dist[u] + 1

q = int(input())
while q > 0:
    visited = [False for i in range(MAX)] 
    dist = [0 for i in range(MAX)] 
    graph = [[] for i in range(MAX)]
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    s = int(input())
    BFS(s)
    for i in range(1, V + 1):
        if (i != s):
            if (dist[i] == 0):
                print(-1, end = " ")
            else:
                print(dist[i] * 6, end = " ")

    print()
    q -= 1