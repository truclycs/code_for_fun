import sys 
sys.setrecursionlimit(1000000000)
INF = 1000000009
MAX = 100000 

def makeSet(v):
    global parent, ranks
    parent = [i for i in range(v + 1)]
    ranks = [0 for i in range(v + 1)]
    
def findSet(u): 
    st = []
    while u != parent[u]:
        st.append(u)
        u = parent[u]
    for i in st:
        parent[i] = parent[u]
    return parent[u]

def unionSet(u, v):
	up = findSet(u)
	vp = findSet(v)
	if up == vp:
		return	
	if ranks[up] > ranks[vp]:
		parent[vp] = up
	else:
		if ranks[up] < ranks[vp]:
			parent[up] = vp
		else:
			parent[up] = vp 
			ranks[vp] += 1

def Kruskal(V): 
    graph.sort()
    i = cnt = res = 0
    while (cnt != V - 1):
        w, u, v = graph[i]
        i += 1
        u = findSet(u)
        v = findSet(v)
        if u != v:
            cnt += 1
            unionSet(u, v)
            res += w
    return res

T = int(input())
for t in range(T): 
	graph = []
	st = input() 
	s = list(st.split()) 
	others = s[0]
	V = int(others)
	s[0] = "0000" 
	
	for i in range(1, V):
		for j in range(i + 1, V + 1):
			sum = 0
			for k in range(4):
				tmp = abs(ord(s[i][k]) - ord(s[j][k]))
				if tmp > 5:
					tmp = 10 - tmp
				sum += tmp
			graph.append((sum, i, j))
			
	makeSet(V)
	res = Kruskal(V)
	mini = 60
	for i in range(1, V + 1): 
		sum = 0
		for k in range(4): 
			tmp = abs(ord(s[i][k]) - 48)
			if tmp > 5:
				tmp = 10 - tmp
			sum += tmp 
		if mini > sum:
			mini = sum
	
	print(res + mini)
