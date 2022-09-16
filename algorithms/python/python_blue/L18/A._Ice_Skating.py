MAX = 101
parent = []

def makeSet():
    global parent
    parent = [i for i in range(MAX + 1)]

def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    parent[up] = vp

makeSet()
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j]:
            unionSet(i, j)

res = 0
for i in range(n):
    if parent[i] == i:
        res += 1

print(res - 1)