import sys
sys.setrecursionlimit(10000000)
dx = [-1,1,2,2,1,-1,-2,-2]
dy = [-2,-2,-1,1,2,2,1,-1]
MAX = 11
visited = [[False for i in range(MAX)] for j in range(MAX)]
chessboard = [[0 for i in range(MAX)] for j in range(MAX)]

def DFS(u, v):
    res = 0 
    visited[u][v] = True
    for i in range(8):
        x = u + dx[i]
        y = v + dy[i]
        if 0 <= x < 10 and 0 <= y < 10 and chessboard[x][y] == 1 and not visited[x][y]:
            res = max(res, DFS(x, y))
    visited[u][v] = False
    return res + 1

Case = 0
while True:
    x = list(map(int, input().split()))
    if x[0] == 0:
        break
    visited = [[False for i in range(MAX)] for j in range(MAX)]
    chessboard = [[0 for i in range(MAX)] for j in range(MAX)]
    n = x[0]
    m = 0
    Case += 1
    for i in range(n):
        u = x[i * 2 + 1]
        v = x[i * 2 + 2]
        for j in range(v):
            chessboard[i][u + j] = 1
        m += v

    res = DFS(0, 0)
    print("Case", Case, end = "")
    print(",", m - res, end = " ")
    if m - res == 1:
        print("square can not be reached.")
    else:
        print("squares can not be reached.")