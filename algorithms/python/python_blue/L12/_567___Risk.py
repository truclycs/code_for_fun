import sys
MAX = 21
INF = 10 ** 9

def FloydWarshall(graph, dist):
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

Case = 0
while (True):
    try:
        n = MAX
        graph = [[INF for i in range(n)] for j in range(n)]
        dist = [[0 for i in range(n)] for j in range(n)]

        for i in range(1, n - 1):
            x = list(map(int, input().split()))
            for j in x[1:]:
                graph[i][j] = graph[j][i] = 1

        FloydWarshall(graph, dist)

        Case += 1
        print("Test Set #" + str(Case))
        m = int(input())
        for i in range(m):
            u, v = map(int, input().split())
            print('%2d to %2d: %d' % (u, v, dist[u][v]))
        print()
    except EOFError:
        break