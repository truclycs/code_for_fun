import queue

def BFS(graph, s, dist):
    q = queue.Queue()
    dist[s] = 0
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if dist[v] == 'undefined':
                dist[v] = dist[u] + 1
                q.put(v)
    return dist

n = int(input())
d = dict()
cnt = 0
graph = []
for _ in range(n):
    l = input().split()
    v = []
    for name in l:
        if name in d:
            id = d[name]
        else:
            d[name] = cnt
            id = cnt
            cnt += 1
            graph.append([])
        v.append(id)
    
    for x in v:
        for y in v:
            if x != y:
                graph[x].append(y)
                
dist = ['undefined' for i in range(cnt)]
if 'Isenbaev' in d:
    dist = BFS(graph, d['Isenbaev'], dist)
a = []
for name in d:
    a.append(name)
a.sort()
for name in a:
    print(name + ' ' + str(dist[d[name]]))

