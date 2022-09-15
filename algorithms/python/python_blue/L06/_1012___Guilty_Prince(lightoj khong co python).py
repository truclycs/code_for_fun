import queue

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

def BFS(s):
    count = 1
    q = queue.Queue()
    q.put(s)
    visited[s.x][s.y] = True
    while q.qsize() > 0:
        u = q.get()
        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]
            if x >= 0 and x < n and y >= 0 and y < m:
                if not visited[x][y] and a[x][y] == '.':
                    visited[x][y] = True
                    q.put(Point(x, y))
                    count += 1
    return count

t = int(input())
Case = 0

while t > 0:
    t -= 1
    points = []
    m, n = map(int, input().split())
    a = []
    for i in range(n):
        line = input()
        a.append(line)
    visited = [[False for i in range(21)] for j in range(21)]
    Case += 1 
    print("Case", Case, end = ": ")
    for i in range(n):
        for j in range(m):
            if a[i][j] == '@':
                print(BFS(Point(i, j)))
                break
