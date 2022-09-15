import sys
sys.setrecursionlimit(1000000)
dx = [0, 0, 1, -1, 1, 1, -1,-1]
dy = [1, -1, 0, 0, 1, -1, 1,-1]
MAX = 101
string = "ALLIZZWELL"

def DFS(x, y, len):
    global flag
    visited[x][y] = True
    if len == 10:
        flag = True
        return True
    for i in range(8):
        u = x + dx[i]
        v = y + dy[i]
        if 0 <= u < r and 0 <= v < c and not visited[u][v]:
            if matrix[u][v] == string[len]:
                DFS(u, v, len + 1)
    visited[x][y] = False

t = int(input())
while t:
    t -= 1
    r, c = map(int, input().split())
    matrix = []
    for i in range(r):
        x = input()
        matrix.append(x)  

    visited = [[False for i in range(MAX)] for j in range(MAX)]
    flag = False
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'A':
                if DFS(i, j, 1):
                    flag = True
                    break
    x = input()
    if flag:
        print("YES")
    else:
        print("NO")

