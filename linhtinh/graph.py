with open('input.txt', 'r') as f:
    inp = f.read().split('\n')


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


def minimum_tree(graph):
    


graph = []
for line in inp:
    u, v, w = line.split(', ')
    graph.append(Edge(int(u), int(v), int(w)))


graph_edge = {}
for e in graph:
    if e.u in graph_edge:
        graph_edge[e.u].append((e.v, e.w))
    else:
        graph_edge[e.u] = [(e.v, e.w)]

    if e.v in graph_edge:
        graph_edge[e.v].append((e.u, e.w))
    else:
        graph_edge[e.v] = [(e.u, e.w)]

print(graph_edge[3])    
