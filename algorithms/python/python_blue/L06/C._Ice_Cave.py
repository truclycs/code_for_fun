import queue
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def BFS(s, f):
    q = queue.Queue()
    q.put(s)
    a[s.x][s.y] = 0
    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if a[x][y] == 0:
                    if x == f.x and y == f.y:
                        return True
                else:
                    a[x][y] = 0
                    q.put(Point(x, y))
    return False

n, m = map(int, input().split())
x = []
for i in range(n):
    line = input()
    x.append(line)

a = []
for i in range(n):
    b = []
    for j in range(m):
        if x[i][j] == 'X':
            b.append(0)
        else:
            b.append(1)
    a.append(b)

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
if BFS(Point(r1 - 1, c1 - 1), Point(r2 - 1, c2 - 1)):
    print("YES")
else:
    print("NO")