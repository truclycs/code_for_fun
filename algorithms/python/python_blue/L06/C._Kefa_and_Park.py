import queue
MAX = 100001
 
def BFS(s):
    res = 0
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    if a[s] == 1:
        cat[s] = 1
    while q.qsize() > 0:
        u = q.get();
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                if a[v] == 1:
                    cat[v] = cat[u] + 1
                if cat[v] <= m:
                    if (len(graph[v]) == 1):
                        res += 1
                    else :
                        q.put(v)
    return res

visited = [False] * MAX
cat = [0] * MAX
graph = [[] for i in range(MAX)]
n, m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)
print(BFS(0))