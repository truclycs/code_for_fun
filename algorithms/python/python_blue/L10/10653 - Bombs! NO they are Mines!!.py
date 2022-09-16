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
    while not q.empty():
        u = q.get()
        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]
            if 0 <= x < R and 0 <= y < C:
                if not visited[x][y] and maze[x][y] == 0:
                    visited[x][y] = True
                    q.put(Point(x, y))
                    path[x][y] = i

def getTime(s, f):
    res = 0
    while s.x != f.x or s.y != f.y:
        tmp = path[f.x][f.y]
        f.x -= dx[tmp]
        f.y -= dy[tmp]
        res += 1
    return res 

while True:
    R, C = map(int, input().split())
    maze = [[0 for i in range(R)] for j in range(C)]
    visited = [[False for i in range(R)] for j in range(C)]
    path = [[0 for i in range(R)] for j in range(C)]
    if R == C == 0:
        break
    rows = int(input())
    for i in range(rows):
        x = list(map(int, input().split()))
        for c in x[1:]:
            maze[x[0]][c] = 1

    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())
    s = Point(sx, sy)
    f = Point(fx, fy)
    BFS(s, f)
    print(getTime(s, f))
