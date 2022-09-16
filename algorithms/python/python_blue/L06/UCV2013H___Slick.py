import queue
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def BFS(s):
    count = 1
    q = []
    q.append(s)
    visited[s.x][s.y] = True
    while len(q) > 0:
        u = q[0]
        q = q[1:len(q)]
        for i in range(4):
            x = u.x + dx[i]
            y = u.y + dy[i]
            if x >= 0 and x < n and y >= 0 and y < m:
                if not visited[x][y] and a[x][y] == 1:
                    visited[x][y] = True
                    q.append(Point(x, y))
                    count += 1
    if count in cnt:
        cnt[count] += 1
    else:
        cnt[count] = 1
    

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = []
    cnt = {}
    visited = [[False for i in range(n)] for j in range(m)]
    for i in range(n):
        line = list(map(int, input().split()))
        a.append(line)
    countt = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1 and not visited[i][j]:
                countt += 1
                BFS(Point(i, j))
    print(countt)
    keys = sorted(cnt.keys()) 
    for i in keys:
        if cnt[i] > 0:
            print(i, cnt[i])

