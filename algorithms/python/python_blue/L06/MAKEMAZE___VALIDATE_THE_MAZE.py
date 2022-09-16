import queue

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def BFS(s, f):
    q = queue.Queue()
    q.put(s)
    visited[s.x][s.y] = True
    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]
            if x >= 0 and x < n and y >= 0 and y < m:
                if not visited[x][y] and maze[x][y] == '.':
                    visited[x][y] = True
                    if x == f.x and y == f.y:
                        return True
                    q.put(Point(x, y))
    return False

t = int(input())

while t > 0:
    t -= 1
    points = []
    n, m = map(int, input().split())
    maze = []
    for i in range(n):
        line = input()
        maze.append(line)
    visited = [[False for i in range(21)] for j in range(21)]
    for i in range(n):
        for j in range(m):
            if maze[i][j] == '.' and (i == 0 or i == n - 1 or j == 0 or j == m - 1):
                points.append(Point(i, j))

    if len(points) == 2:
        if BFS(points[0], points[1]):
            print("valid")
        else:
            print("invalid")
    else:
        print("invalid")