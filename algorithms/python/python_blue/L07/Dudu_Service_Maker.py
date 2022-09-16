import sys
sys.setrecursionlimit(100000000)

def DFS(u):
    visited[u] = 1
    for i in range(len(graph[u])):
        v = graph[u][i]
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if (DFS(v)):
                return True
    visited[u] = 2
    return False

T = int(input())
while T:
    T -= 1
    n, m = map(int, input().split())
    visited = [0 for i in range(n + 1)]
    graph = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)

    cycle = False
    for i in range(n):
        if not visited[i]:
            cycle = DFS(i)
            if cycle:
                break
    if cycle:
        print("SIM")
    else:
        print("NAO")
