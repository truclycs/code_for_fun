import sys
sys.setrecursionlimit(1000000000)
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

class node:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def DFS(x, y):
    global cnt
    global flag
    cnt += 1
    visited[x][y] = True
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or ty < 0 or tx >= n or ty >= m:
            flag = True
            continue
        if map[tx][ty] == '*' or visited[tx][ty]:
            continue
        DFS(tx, ty)

def DFS1(x, y):
    map[x][y] = '*'
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]
        if tx < 0 or ty < 0 or tx >= n or ty >= m:
            continue
        if map[tx][ty] == '*':
            continue
        DFS1(tx, ty)


n, m, k = map(int, input().split())
map = []
for i in range(n):
    x = list(input())
    map.append(x)

visited = [[False for i in range(101)] for j in range(101)]

a = []
for i in range(n):
    for j in range(m):
       if not visited[i][j] and map[i][j] == '.':
            cnt = 0
            flag = False
            DFS(i, j)
            if not flag:
                a.append(node(i, j, cnt))

a = sorted(a, key = lambda node: node.value, reverse = False)

res = 0
for i in range(len(a) - k):
    res += a[i].value
    DFS1(a[i].x, a[i].y)

print(res)
for i in range(n):
    for j in range(m):
        print(map[i][j], end = "")
    print()



