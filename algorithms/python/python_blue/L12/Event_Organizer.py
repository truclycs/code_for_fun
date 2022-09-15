INF = 10 ** 9
MAX = 49
def FloydWarshall(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i <= k <= j and  dist[i][j] < dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

Case = int(input())
for Case in range(1, Case + 1):
    dist = [[0] * MAX for i in range(MAX)]
    n = int(input())
    for i in range(n):
        s, e, c = map(int, input().split())
        if c > dist[s][e]:
            dist[s][e] = c
    FloydWarshall(dist)
    print(dist[0][48])

