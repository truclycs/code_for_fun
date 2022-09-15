MAX = 100001
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

t = int(input())
while t > 0:
    line = input()
    n = int(input())
    e = int(input())
    graph = [[] for i in range(MAX)]
    visited = [False] *  MAX
    for i in range(e):
        a, b = map(int, input().split(' '))
        graph[a].append(b)
        graph[b].append(a)
 
    res = 0
    for i in range(n):
        if not visited[i]:
            res += 1
            DFS(i)
    print(res)
    t -= 1
