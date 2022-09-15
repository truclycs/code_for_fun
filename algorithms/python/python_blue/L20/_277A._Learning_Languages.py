MAX = 201

def DFS(u):
    visited[u] = True
    for i in range(len(graph[u])):
        v = graph[u][i]
        if not visited[v]:  
            DFS(v)

n, m = map(int, input().split())
visited = [False for i in range(MAX)]
graph = [[] for i in range(MAX)]

res = 0
for i in range(n):
    l = input().split()
    if int(l[0]) == 0:
        res += 1

    for j in range(int(l[0])):
        x = int(l[j + 1])
        graph[i].append(x + 100)
        graph[x + 100].append(i)

if res == n:
    print(n)
else:
    res = 0
    for i in range(n):
        if not visited[i]:
            res += 1
            DFS(i)
    print(res - 1)