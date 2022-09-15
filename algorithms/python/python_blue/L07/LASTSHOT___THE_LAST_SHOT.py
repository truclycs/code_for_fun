import sys
sys.setrecursionlimit(10000)
class Scanner:
	def __init__(self, istream):
		self.tokenizer = Scanner.__tokenizer__(istream)
	def __tokenizer__(istream):
		for line in istream:
			for token in line.strip().split():
				yield token
	def next(self):
		return self.tokenizer.__next__()

def DFS(u):
    global cnt
    visited[u] = True
    for i in range(len(graph[u])):
        v = graph[u][i]
        if not visited[v]:
            cnt += 1    
            DFS(v)

sc = Scanner(sys.stdin)
n = int(sc.next())
m = int(sc.next())
graph = [[] for i in range(n + 1)]
for i in range(m):
    u = int(sc.next())
    v = int(sc.next())
    u -= 1
    v -= 1
    graph[u].append(v)

res = 0
for i in range(0, n):
    visited = [False] * (n + 1)
    cnt = 1
    DFS(i)
    res = max(res, cnt)
print(res)