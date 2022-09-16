MAX = 1001
visited = [False] * MAX
graph = [[] for i in range(MAX)]
dist = [0] * MAX

def DFS(src):
    s = []
    s.append(src)
    visited[src] = True
    while len(s) > 0:
        u = s[-1]
        s.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                s.append(v)
                dist[v] = dist[u] + 1
                    
n = int(input())
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
DFS(1)
min_dist = MAX * MAX
q = int(input())
for i in range(q):
    x = int(input())
    if dist[x] < min_dist:
        min_dist = dist[x]
        res = x
print(res)
