import queue
dist = [-1 for i in range(100001)]
q = queue.Queue()

def BFS(s, f):
    q.put(s)
    dist[s] = 0
    while q.qsize() > 0:
        u = q.get()
        for x in a:
            v = (u * x) % 100000
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.put(v)
                if v == f:
                    return dist[f]
    return -1
    

x, y = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
print(BFS(x, y))

